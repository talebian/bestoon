#!/bin/bash
mytoken=1234567
curl --data "token=$mytoken&amount=$2&text=$1" http://localhost:8000/submit/expense/
