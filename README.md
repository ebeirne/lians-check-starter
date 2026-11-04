# Try Lians in 2 minutes

[Lians](https://www.lians.ai) checks each pull request against the ticket it closes. This repo gives you a sample ticket and a PR that passes CI but misses part of it, so you can watch a real check on your own repo.

No API key and no workflow file needed.

## Steps

1. **Click "Use this template" → "Create a new repository".** Tick **Include all branches**, or the sample PR won't be there.
2. **[Install the Lians GitHub App](https://www.lians.ai/install)** and pick only your new repo.
3. **[Open the sample ticket](../../issues/new?template=try-lians.md)** and submit it as is. It has to be issue #1 in your repo.
4. **[Open the sample PR](../../compare/main...agent-attempt?expand=1)** and submit that as is too. It says `Fixes #1`, and its tests pass.

CI goes green, and a Lians comment appears within about a minute. It marks each requirement met or missed, with the evidence.

## Then change the ticket

Edit issue #1 and add a line, like:

> 5. GBP amounts look like `£12.34`.

Lians re-checks the open PR and tags the author with what now needs a look.

## What the sample PR gets wrong

It handles USD and EUR, and its two tests pass. It shows refunds with a minus sign instead of parentheses, and an unknown currency raises `KeyError`, not `ValueError`. Nothing in CI catches either one.

## Use it on your real repos

[Install the App](https://www.lians.ai/install) on any repo. Link a ticket from a PR with `Fixes #123`. It's free for everyone through January 31, 2027, and free after that for public repos under an OSI-approved open-source license. Docs: [ebeirne/lians-check](https://github.com/ebeirne/lians-check).

The sample code here is MIT licensed. A real run on another repo: [ebeirne/lians-demo#2](https://github.com/ebeirne/lians-demo/pull/2).
