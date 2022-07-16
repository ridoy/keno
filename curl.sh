#!/bin/bash
# Curl keno results from 1/13/2022 to 7/15/2022
i=2163853
# new min = 2098670
while ((i >= 2098750)); do
     curl "https://keno.prod.mdlotto.mindgrb.io/api/past_numbers/K/${i}/20" > "${i}.txt"
     i=$((i-20))
     echo $i
done

