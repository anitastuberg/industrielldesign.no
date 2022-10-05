#!/bin/bash
export LDFLAGS="-L/opt/homebrew/opt/openssl@1.1/lib -L/opt/homebrew/opt/python@3.8/lib -L/opt/homebrew/opt/icu4c/lib"
export CPPFLAGS="-I/opt/homebrew/opt/openssl@1.1/include -I/opt/homebrew/opt/icu4c/include"
export PATH=/opt/homebrew/opt/postgresql@11/bin:$PATH