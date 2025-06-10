# Settings

## Setting Debugging Preference

> $ export AGENTIC_DEBUG=agents|tools|llm|all

you can combine flags or just use 'all' for everything.

> $ export AGENTIC_OVERRIDE_MODEL=xx

Force all agents to use the indicated model regardless of their configuration. Uses the `Litellm` 
qualified model names.

## Configuring the database for thread logging

Set `AGENTIC_DATABASE_URL` to configure the db connection for storing Agent threads and thread logs.

> $ export AGENTIC_DATABASE_URL=postgres://...