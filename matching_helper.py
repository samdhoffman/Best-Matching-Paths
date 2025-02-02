def add_matches(results, cur_matches):
    if not cur_matches:
        results.append("NO MATCH")
    elif min(cur_matches.keys()) == 0:
        results.append(cur_matches[0][0])
    else:
        min_wildcards = min(cur_matches.keys())
        best_match = get_best_match(cur_matches[min_wildcards], 0, "*")
        results.append(best_match)
        
    return results

# this method gets called recursively to find best match when multiple patterns 
# have thier leftmost "*" at the same position
def get_best_match(matches, start_index, target):
    if len(matches) == 1:
        return matches[0]
    
    cur_matches = matches
    
    left = cur_matches[0][start_index:].index(target)
    result = {}
    
    for i in range (0, len(cur_matches)):
        if cur_matches[i][start_index:].index("*") >= left:
            left = cur_matches[i][start_index:].index("*")
            if left in result and cur_matches[i] not in result[left]:
                result[left].append(cur_matches[i])
            else:
                result[left] = [cur_matches[i]]
        
    if len(result[left]) > 1:
        # recursive call
        return get_best_match(result[left], start_index + 1, "*")
    else:
        return result[left][0]

# this method is where most of the matching work occurs
# algorithmic complexity is On^2
def get_matching_patterns(patterns, paths):
    if not patterns or not paths:
      return ["NO MATCH"]

    results = []
    delimiter = ','
    
    for p in paths:
        # remove leading and trailing "/"
        if p[0] == "/" or p[-1] == "/":
            p = p.strip("/")
            
        pathArr = p.split("/")
        
        matches = {} # i am using a dict to take advantage of O(1) lookup and insertion time
        
        for pattern in patterns:
            patternArr = pattern.split(",")
            
            if len(patternArr) == len(pathArr):
                cur_pos = 0
                cur_match = []
                
                # will use wildcard_count as key in matches dict
                # this way it will be easy to consolidate the patterns 
                # that have the fewest wildcards if any
                wildcard_count = 0 
                
                while cur_pos < len(patternArr):
                    if patternArr[cur_pos] == "*":
                        cur_match += patternArr[cur_pos]
                        wildcard_count += 1
                    elif patternArr[cur_pos] == pathArr[cur_pos]:
                        cur_match.append(patternArr[cur_pos])
                    else:
                        break

                    cur_pos += 1
                
                if len(cur_match) == len(pathArr):
                    cur_match = delimiter.join(cur_match)
                    if wildcard_count in matches:
                        matches[wildcard_count].append(cur_match)
                    else:
                        matches[wildcard_count] = [cur_match]
        
        results = add_matches(results, matches)
        
    return results