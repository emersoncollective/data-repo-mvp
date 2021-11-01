def remove_impossible_filter_combinations(all_filter_combinations, negate_rules):
    # Here we iterate over the filter options and get the index
    # of the combinations present in the negate rules above
    remove_idxs = []
    for fs_idx, filter_set in enumerate(all_filter_combinations):
        for negate_rule in negate_rules:
            rule_length = len(negate_rule)
            agreement_length = 0
            for rule_idx, rule_val in negate_rule:
                if filter_set[rule_idx] == rule_val:
                    agreement_length += 1
            if rule_length == agreement_length:
                remove_idxs.append(fs_idx)
    # Remove those options by index
    all_filter_combinations = (
        pd.Series(all_filter_combinations).drop(remove_idxs).tolist()
    )


# # This seems a little complicated but it just python list that holds
# # data on combinations that do not exit.
# # The first item ((1, "Office of Field Operations"), (2, "FMUA"), (3, "Title 42"))
# # just says that Office of Field Operations + FMUA + Title 42 is not a valid combination
# # so don't even try it. The numbers before the text indicate the filter order
# # you can see the filter order by running print(all_filter_columns)
# negate_rules = [
#     ((1, "Office of Field Operations"), (2, "FMUA"), (3, "Title 42")),
#     ((1, "U.S. Border Patrol"), (2, "Accompanied Minors")),
# ]

# all_filter_combinations = remove_impossible_filter_combinations(filter_data['filter_combinations'], negate_rules )
