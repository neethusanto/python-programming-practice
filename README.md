# Python Basics Practical Programming Mastery (180 Questions)

A structured repository containing **180 practical coding questions** (15 questions per core topic across 12 topics) designed to master algorithmic thinking and data structure manipulation from first principles.

> **Key Learning Principle**: All programs are implemented strictly **without relying on high-level shortcut built-in methods** (such as `max()`, `min()`, `sum()`, `math.factorial()`, `math.gcd()`, `str.replace()`, `str.split()`, `str.strip()`, `str.lower()`, `str.upper()`, `list.reverse()`, `list.sort()`, `collections.Counter`, etc.) to foster deep algorithmic comprehension.

---

## Project Overview

| Metric | Details |
| :--- | :--- |
| **Total Topics** | 12 Topics |
| **Questions Per Topic** | 15 Practical Questions |
| **Total Practice Problems** | 180 Individual Scripts |
| **Dependencies** | Python Standard Library (Pure Python 3.8+) |
| **Status** | 100% Tested & Verified Passing |

---

## Directory & Folder Structure

```
Python Basics/
├── .gitignore                   # Ignores __pycache__, venv, and IDE files
├── README.md                    # Project documentation & complete problem index
├── requirements.txt             # Environment specifications
│
├── 01_conditional_statements/   # 15 Questions (decision-making, logic gates)
├── 02_loops/                    # 15 Questions (for/while loops, arithmetic iterations)
├── 03_functions/                # 15 Questions (custom reusable algorithmic routines)
├── 04_strings/                  # 15 Questions (pointer traversal, ASCII conversions)
├── 05_recursion/                # 15 Questions (base cases, call stack recurrence)
├── 06_regular_expressions/      # 15 Questions (pattern matching, validation, extraction)
├── 07_list_comprehension/       # 15 Questions (declarative filtering and mapping)
├── 08_lambda_functions/         # 15 Questions (anonymous functions, closures, higher-order)
├── 09_lists/                    # 15 Questions (in-place mutation, two-pointers, sorting)
├── 10_tuples/                   # 15 Questions (immutable sequences, records, unpacking)
├── 11_sets/                     # 15 Questions (Venn operations from scratch, uniqueness)
└── 12_dictionaries/             # 15 Questions (hash mapping, key-value aggregation)
```

---

## Topics & Problem Directory

### 1. Conditional Statements (`01_conditional_statements/`)
| File | Problem Description |
| :--- | :--- |
| `01_check_positive_negative_zero.py` | Check whether a number is positive, negative, or zero |
| `02_check_even_or_odd.py` | Determine if an integer is even or odd |
| `03_largest_of_three_numbers.py` | Find largest among three numbers without `max()` |
| `04_smallest_of_three_numbers.py` | Find smallest among three numbers without `min()` |
| `05_leap_year_check.py` | Leap year validation rules |
| `06_triangle_type_classifier.py` | Classify triangle as Equilateral, Isosceles, Scalene, or Invalid |
| `07_vowel_or_consonant.py` | Check vowel or consonant without `.lower()` or `.upper()` |
| `08_grading_system.py` | Calculate letter grades from score thresholds |
| `09_voting_eligibility.py` | Verify voting eligibility based on age |
| `10_divisibility_rules.py` | Check divisibility by 5 and 11 |
| `11_quadrant_determiner.py` | Determine 2D Cartesian quadrant of point `(x, y)` |
| `12_simple_calculator.py` | Basic arithmetic calculator without `eval()` |
| `13_quadratic_roots.py` | Find roots of quadratic equation without `math.sqrt()` |
| `14_character_type_detector.py` | Classify uppercase, lowercase, digit, or special symbol |
| `15_tax_calculator.py` | Calculate tiered income tax without built-in libraries |

### 2. Loops (`02_loops/`)
| File | Problem Description |
| :--- | :--- |
| `01_sum_of_n_natural_numbers.py` | Sum of first N natural numbers using a loop |
| `02_factorial_using_loop.py` | Compute factorial iteratively without `math.factorial()` |
| `03_multiplication_table.py` | Generate multiplication table up to 10 |
| `04_reverse_an_integer.py` | Reverse integer using modulo arithmetic without string slicing |
| `05_count_digits_in_number.py` | Count digits without `len()` or `str()` |
| `06_sum_of_digits.py` | Sum of digits via arithmetic without `str()` or `sum()` |
| `07_prime_number_check.py` | Prime number check using loop |
| `08_primes_in_range.py` | Print all prime numbers in range `[start, end]` |
| `09_fibonacci_series_up_to_n_terms.py` | Generate first N Fibonacci numbers iteratively |
| `10_palindrome_number_check.py` | Palindrome number check purely through numeric operations |
| `11_armstrong_number_check.py` | Armstrong number check without `pow()` or string conversion |
| `12_gcd_hcf_euclidean.py` | Find GCD / HCF using Euclidean loop without `math.gcd()` |
| `13_lcm_of_two_numbers.py` | Find LCM using loop and GCD relation without `math.lcm()` |
| `14_number_patterns.py` | Print right-angled number triangle using nested loops |
| `15_star_pyramid_pattern.py` | Print centered star pyramid using nested loops |

### 3. Functions (`03_functions/`)
| File | Problem Description |
| :--- | :--- |
| `01_calculate_power.py` | Calculate base^exp without `**` or `pow()` |
| `02_find_maximum_in_list.py` | Find maximum value in a list without `max()` |
| `03_find_minimum_in_list.py` | Find minimum value in a list without `min()` |
| `04_calculate_list_sum.py` | Sum elements of a list without `sum()` |
| `05_calculate_average.py` | Calculate average without `sum()` or `len()` |
| `06_linear_search.py` | Linear search implementation without `.index()` |
| `07_binary_search.py` | Binary search on sorted list without `bisect` |
| `08_bubble_sort.py` | Bubble sort implementation without `.sort()` or `sorted()` |
| `09_remove_duplicates_from_list.py` | Remove duplicates while preserving order without `set()` |
| `10_reverse_list_in_place.py` | Two-pointer list reverse in-place without `.reverse()` |
| `11_check_list_is_sorted.py` | Check if list is ascendingly sorted |
| `12_count_element_frequency.py` | Count element occurrences without `.count()` |
| `13_find_second_largest.py` | Find second largest element in a single pass |
| `14_merge_two_sorted_lists.py` | Merge two sorted lists into one sorted list |
| `15_swap_two_variables.py` | Variable swap via arithmetic and XOR without temporary variable |

### 4. Strings (`04_strings/`)
| File | Problem Description |
| :--- | :--- |
| `01_string_length.py` | Calculate string length without `len()` |
| `02_reverse_string.py` | Reverse string without `[::-1]` or `reversed()` |
| `03_check_string_palindrome.py` | Palindrome check with two pointers without slicing |
| `04_count_vowels_and_consonants.py` | Count vowels & consonants without `.count()` or case methods |
| `05_to_uppercase.py` | Convert to uppercase using ASCII arithmetic without `.upper()` |
| `06_to_lowercase.py` | Convert to lowercase using ASCII arithmetic without `.lower()` |
| `07_toggle_case.py` | Toggle case of all letters without `.swapcase()` |
| `08_character_frequency_counter.py` | Count character frequencies without `collections.Counter` |
| `09_remove_all_spaces.py` | Remove whitespace without `.replace()` |
| `10_substring_search.py` | Find substring index without `in`, `.find()`, or `.index()` |
| `11_split_string_by_delimiter.py` | Split string by delimiter without `.split()` |
| `12_join_strings.py` | Join list of strings without `.join()` |
| `13_replace_character.py` | Replace character occurrences without `.replace()` |
| `14_strip_leading_trailing_spaces.py` | Strip leading and trailing spaces without `.strip()` |
| `15_check_anagram.py` | Anagram check using character frequency mapping |

### 5. Recursion (`05_recursion/`)
| File | Problem Description |
| :--- | :--- |
| `01_recursive_factorial.py` | Recursive factorial without loops or built-ins |
| `02_recursive_fibonacci.py` | Recursive N-th Fibonacci number |
| `03_recursive_sum_of_natural_numbers.py` | Recursive sum of 1 to N |
| `04_recursive_power.py` | Recursive power (base^exp) handling negative exponents |
| `05_recursive_gcd.py` | Euclidean recursive GCD without `math.gcd()` |
| `06_recursive_sum_of_digits.py` | Recursive sum of digits using arithmetic |
| `07_recursive_count_digits.py` | Recursive digit counter without `len()` |
| `08_recursive_reverse_string.py` | Reverse string recursively without `[::-1]` |
| `09_recursive_string_palindrome.py` | Recursive palindrome check |
| `10_recursive_print_1_to_n.py` | Recursive print 1-to-N and N-to-1 without loops |
| `11_recursive_binary_search.py` | Recursive binary search on sorted collection |
| `12_recursive_list_sum.py` | Recursive list summation without `sum()` |
| `13_recursive_tower_of_hanoi.py` | Classic Tower of Hanoi puzzle with step logging |
| `14_recursive_check_sorted.py` | Check if list is sorted recursively |
| `15_recursive_count_occurrences.py` | Count occurrences of an item in a list recursively |

### 6. Regular Expressions (`06_regular_expressions/`)
| File | Problem Description |
| :--- | :--- |
| `01_extract_all_email_addresses.py` | Extract email addresses matching RFC pattern |
| `02_extract_phone_numbers.py` | Extract standard 10-digit telephone patterns |
| `03_validate_email_format.py` | Strict validation of email strings |
| `04_validate_url.py` | Validate HTTP/HTTPS URLs with query params |
| `05_extract_dates.py` | Extract dates in DD/MM/YYYY or DD-MM-YYYY format |
| `06_remove_special_characters.py` | Sanitize string by removing non-alphanumeric symbols |
| `07_find_all_words_starting_with_vowel.py` | Extract words that start with vowels |
| `08_validate_ipv4_address.py` | Octet boundary range validation (0-255) |
| `09_find_duplicate_words.py` | Find consecutive duplicate words with backreferences |
| `10_validate_strong_password.py` | Regex lookahead enforcement for password policies |
| `11_split_by_multiple_delimiters.py` | Split strings by multiple delimiters (`[,;:\|]`) |
| `12_extract_hashtags_and_mentions.py` | Extract `#hashtags` and `@mentions` |
| `13_replace_multiple_spaces_with_single_space.py` | Normalize irregular spacing to single space |
| `14_find_capitalized_words.py` | Match capitalized proper nouns |
| `15_extract_html_tags_and_content.py` | Parse HTML opening/closing tags and body |

### 7. List Comprehension (`07_list_comprehension/`)
| File | Problem Description |
| :--- | :--- |
| `01_squares_of_numbers.py` | Compute squares from 1 to N |
| `02_filter_even_numbers.py` | Filter even elements using `if` clause |
| `03_filter_odd_numbers.py` | Filter odd elements |
| `04_uppercase_words.py` | Transform words to uppercase via ASCII without `.upper()` |
| `05_lengths_of_strings.py` | Compute length of each string without `len()` |
| `06_filter_words_by_length.py` | Filter words longer than length threshold |
| `07_flatten_2d_matrix.py` | Flatten 2D grid into 1D list |
| `08_transpose_matrix.py` | Swap matrix rows and columns via nested comprehension |
| `09_if_else_even_odd_labels.py` | Conditional value transformation (`if-else` inside comprehension) |
| `10_common_elements_in_two_lists.py` | Find intersection without `set()` |
| `11_cartesian_product.py` | Generate all pair combinations |
| `12_filter_prime_numbers.py` | Filter primes in range using comprehension |
| `13_extract_digits_from_string.py` | Extract numeric characters as integers |
| `14_filter_words_starting_with_vowel.py` | Extract words beginning with vowel characters |
| `15_remove_vowels_from_string.py` | Consonant preservation / vowel removal |

### 8. Lambda Functions (`08_lambda_functions/`)
| File | Problem Description |
| :--- | :--- |
| `01_square_a_number.py` | Single-parameter arithmetic lambda |
| `02_add_two_numbers.py` | Multi-parameter lambda function |
| `03_check_even_or_odd.py` | Conditional ternary lambda expression |
| `04_maximum_of_two_numbers.py` | Max selector without `max()` |
| `05_filter_even_numbers_using_filter.py` | Filter predicate lambda |
| `06_map_cubes_using_map.py` | Map transformation lambda |
| `07_sort_tuples_by_second_element.py` | Key extraction lambda for tuple sorting |
| `08_sort_dictionary_by_values.py` | Sort key selector lambda for dictionaries |
| `09_sort_strings_by_length.py` | String length selector lambda |
| `10_custom_reduce_multiplication.py` | Accumulator lambda for custom reduce |
| `11_check_string_palindrome_lambda.py` | Self-contained palindrome check lambda |
| `12_celsius_to_fahrenheit.py` | Unit conversion formula lambda |
| `13_extract_first_and_last_characters.py` | Multi-value extraction lambda |
| `14_filter_palindromes_from_list.py` | Filter word list for palindromes |
| `15_higher_order_function_multiplier.py` | Factory function returning multiplier closures |

### 9. Lists (`09_lists/`)
| File | Problem Description |
| :--- | :--- |
| `01_sum_and_average_of_list.py` | Calculate sum and average in one pass without `sum()` / `len()` |
| `02_find_max_and_min.py` | Find min and max in a single iteration |
| `03_reverse_list.py` | In-place two-pointer list reversal |
| `04_remove_duplicates.py` | Remove duplicates maintaining order without `set()` |
| `05_second_largest_element.py` | Second largest distinct element in O(N) |
| `06_rotate_list_by_k_positions.py` | Cyclic right rotation by K steps without slice tricks |
| `07_count_frequency_of_elements.py` | Element frequency table without `count()` |
| `08_merge_two_sorted_lists.py` | Merge two sorted lists in O(N+M) |
| `09_separate_even_and_odd.py` | Partition list into evens and odds |
| `10_intersection_of_two_lists.py` | Unique common elements |
| `11_check_subset_list.py` | Subset containment check |
| `12_cumulative_sum_list.py` | Running prefix sum list |
| `13_chunk_list_into_sublists.py` | Partition list into chunks of size K |
| `14_bubble_sort_list.py` | Bubble sort implementation |
| `15_flatten_nested_list.py` | Recursive flattening of arbitrary nested lists |

### 10. Tuples (`10_tuples/`)
| File | Problem Description |
| :--- | :--- |
| `01_tuple_length.py` | Count tuple length without `len()` |
| `02_find_max_min_in_tuple.py` | Max and min values in tuple |
| `03_count_element_in_tuple.py` | Count occurrences without `tuple.count()` |
| `04_find_index_of_element.py` | Linear search index without `tuple.index()` |
| `05_reverse_a_tuple.py` | Reverse tuple elements without `reversed()` |
| `06_check_element_exists.py` | Membership check without `in` |
| `07_convert_tuple_to_string.py` | Convert character tuple to string without `.join()` |
| `08_merge_two_tuples.py` | Merge two tuples without `+` operator |
| `09_unpack_tuple_elements.py` | Positional record unpacking |
| `10_remove_item_from_tuple.py` | Delete element from immutable tuple |
| `11_slice_tuple_manually.py` | Manual index boundary slicing |
| `12_check_all_elements_same.py` | Homogeneity check |
| `13_find_repeated_items_in_tuple.py` | Duplicate detector in tuple |
| `14_sort_tuple_of_tuples_by_index.py` | Sort nested records by index column |
| `15_convert_list_of_tuples_to_dictionary.py` | Key-value pair builder without `dict()` |

### 11. Sets (`11_sets/`)
| File | Problem Description |
| :--- | :--- |
| `01_set_union.py` | Union without `.union()` or `\|` |
| `02_set_intersection.py` | Intersection without `.intersection()` or `&` |
| `03_set_difference.py` | Difference without `.difference()` or `-` |
| `04_symmetric_difference.py` | Symmetric difference without `^` |
| `05_check_subset.py` | Subset validation without `.issubset()` |
| `06_check_superset.py` | Superset validation without `.issuperset()` |
| `07_check_disjoint_sets.py` | Disjoint set check without `.isdisjoint()` |
| `08_remove_element_from_set.py` | Element removal without `.remove()` or `.discard()` |
| `09_find_max_and_min_in_set.py` | Max and min element discovery |
| `10_set_size_counter.py` | Set size counting without `len()` |
| `11_check_common_elements_in_three_sets.py` | 3-way set intersection |
| `12_deduplicate_list_to_set.py` | Manual set population from list |
| `13_find_unique_elements_in_string.py` | Extract unique characters without `set(string)` |
| `14_cartesian_product_of_sets.py` | Pair combinations between sets |
| `15_power_set_generator.py` | Generate all `2^N` subsets without itertools |

### 12. Dictionaries (`12_dictionaries/`)
| File | Problem Description |
| :--- | :--- |
| `01_merge_two_dictionaries.py` | Combine dictionaries without `.update()` or `**` |
| `02_invert_dictionary.py` | Swap keys and values without dict comprehension |
| `03_key_with_maximum_value.py` | Key with maximum value without `max()` |
| `04_key_with_minimum_value.py` | Key with minimum value without `min()` |
| `05_word_frequency_counter.py` | Word frequency hashmap |
| `06_character_frequency_counter.py` | Character frequency hashmap |
| `07_remove_key_from_dictionary.py` | Delete key without `.pop()` or `del` |
| `08_filter_dictionary_by_value.py` | Filter entries by value threshold |
| `09_sort_dictionary_by_keys.py` | Sort dictionary by keys |
| `10_sort_dictionary_by_values.py` | Sort dictionary by values |
| `11_check_key_exists.py` | Key existence lookup without `in` |
| `12_sum_all_values_in_dict.py` | Sum all numeric values without `sum()` |
| `13_combine_two_dicts_adding_values.py` | Merge dictionaries accumulating matching keys |
| `14_group_anagrams_into_dict.py` | Group anagrams using frequency key |
| `15_flatten_nested_dictionary.py` | Flatten deep nested maps with dot paths |

---

## Getting Started & Execution

### Prerequisites
- Python 3.8 or newer installed on your machine.

### Running Any Problem
Each file is completely self-contained with comprehensive test cases defined under `if __name__ == "__main__":`. Run any file directly from your terminal:

```bash
# Run a specific script
python 01_conditional_statements/01_check_positive_negative_zero.py
python 06_regular_expressions/01_extract_all_email_addresses.py
python 07_list_comprehension/07_flatten_2d_matrix.py
python 08_lambda_functions/08_sort_dictionary_by_values.py
python 09_lists/06_rotate_list_by_k_positions.py
python 10_tuples/14_sort_tuple_of_tuples_by_index.py
python 11_sets/15_power_set_generator.py
python 12_dictionaries/14_group_anagrams_into_dict.py
```
