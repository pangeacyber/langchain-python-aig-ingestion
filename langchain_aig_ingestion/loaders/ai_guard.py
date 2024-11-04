from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path
from typing import override

from langchain_community.document_loaders.text import TextLoader
from langchain_core.documents import Document
from pangea import PangeaConfig
from pangea.services import AIGuard
from pydantic import SecretStr


class GuardedTextLoader(TextLoader):
    _client: AIGuard

    def __init__(
        self,
        file_path: str | Path,
        *,
        encoding: str | None = None,
        autodetect_encoding: bool = False,
        token: SecretStr,
        domain: str = "aws.us.pangea.cloud",
    ) -> None:
        """
        Args:
            token: Pangea AI Guard API token.
            domain: Pangea API domain.
        """

        super().__init__(file_path=file_path, encoding=encoding, autodetect_encoding=autodetect_encoding)
        self._client = AIGuard(token=token.get_secret_value(), config=PangeaConfig(domain=domain))

    @override
    def lazy_load(self) -> Iterator[Document]:
        for doc in super().lazy_load():
            guarded = self._client.guard_text(doc.page_content)
            assert guarded.result

            if guarded.result.redacted_prompt:
                yield doc.model_copy(update={"page_content": guarded.result.redacted_prompt})
                continue

            yield doc
