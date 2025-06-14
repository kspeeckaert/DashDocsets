#!/bin/bash

wget \
-e robots=off \
--mirror \
--page-requisites \
--convert-links \
--no-parent \
--restrict-file-names=windows \
--adjust-extension \
--user-agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15" \
--accept-regex "learn.microsoft.com/(en-us/kusto/(management|query)/.*\?view=azure-data-explorer$|static/assets/.*)" \
--random-wait \
--wait 3 \
--no-verbose \
https://learn.microsoft.com/en-us/kusto/\?view=azure-data-explorer
