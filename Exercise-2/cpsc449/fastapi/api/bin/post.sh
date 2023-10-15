#!/bin/sh

# http --verbose POST localhost:5000/books/ @"$1"
http --verbose POST localhost:5200/api/books/ @"$1"
