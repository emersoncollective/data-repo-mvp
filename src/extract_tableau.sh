#!/bin/bash

# echo "Processing Dashboard 1"
# python src/cbp_tableau_scraping.py \
#      --url https://publicstats.cbp.gov/t/PublicFacing/views/CBPSBOEnforcementActionsDashboardsOCTFY22/SBOEncounters10935 \
#      --data_element "SBO Table" \
#      --skip_filters '["Fiscal Year"]' \
#      --label 'cbp_encounters_dashboard_1'

echo "Processing Dashboard 2"
python src/cbp_tableau_scraping.py \
    --url https://publicstats.cbp.gov/t/PublicFacing/views/CBPSBOEnforcementActionsDashboardsOCTFY22/SBObyMonthDemo10935 \
    --data_element "Demo FYTD by Month (2)" \
    --skip_filters '["Demographic"]' \
    --label 'cbp_encounters_dashboard_2'