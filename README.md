# AI Guard Data Ingestion for LangChain in Python

An example Python app that demonstrates integrating Pangea's [AI Guard][]
service into a LangChain app to protect data ingestion.

In this case, the data to be ingested consists of articles about authentication
from our [Secure by Design Hub][] included in `langchain_aig_ingestion/data`.

## Prerequisites

- Python v3.12 or greater.
- pip v24.2 or [uv][] v0.5.11.
- A [Pangea account][Pangea signup] with AI Guard enabled.
- An [OpenAI API key][OpenAI API keys].

## Setup

```shell
git clone https://github.com/pangeacyber/langchain-python-aig-ingestion.git
cd langchain-python-aig-ingestion
```

If using pip:

```shell
python -m venv .venv
source .venv/bin/activate
pip install .
```

Or, if using uv:

```shell
uv sync
source .venv/bin/activate
```

The sample can then be executed with:

```shell
python -m langchain_aig_ingestion "What do you know about OAuth?"
```

_Note:_ Because our context is limited to the authentication articles mentioned
above, if you ask a question outside that context, you will get some variation
of "I don't know."

## Usage

```
Usage: python -m langchain_aig_ingestion [OPTIONS] PROMPT

Options:
  --model TEXT             OpenAI model.  [default: gpt-4o-mini; required]
  --ai-guard-token SECRET  Pangea AI Guard API token. May also be set via the
                           `PANGEA_AI_GUARD_TOKEN` environment variable.
                           [required]
  --pangea-domain TEXT     Pangea API domain. May also be set via the
                           `PANGEA_DOMAIN` environment variable.  [default:
                           aws.us.pangea.cloud; required]
  --openai-api-key SECRET  OpenAI API key. May also be set via the
                           `OPENAI_API_KEY` environment variable.  [required]
  --help                   Show this message and exit.
```

### Example Input

```shell
python -m langchain_aig_ingestion "What do you know about OAuth?"
```

### Sample Output

OAuth 2.0 is a protocol primarily focused on authorization and resource access
control, while OpenID Connect (OIDC) is built on top of OAuth 2.0 and
specializes in user authentication. OIDC allows applications to verify a user's
identity through a trusted identity provider, ensuring that apps do not handle
sensitive user credentials directly. This combination provides a secure and
convenient authentication process for users accessing online services.

[AI Guard]: https://pangea.cloud/docs/ai-guard/
[Pangea signup]: https://pangea.cloud/signup
[Secure by Design Hub]: https://pangea.cloud/securebydesign/
[OpenAI API keys]: https://platform.openai.com/api-keys
[uv]: https://docs.astral.sh/uv/
