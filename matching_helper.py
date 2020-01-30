patterns = ["*,b,*", "a,*,*", "*,*,c", "foo,bar,baz", "w,x,*,*", "*,x,y,z"]
paths = ["/w/x/y/z/", "a/b/c", "foo/", "foo/bar/", "foo/bar/baz/"]


def add_matches(results, cur_matches):
    if not cur_matches:
        results.append("NO MATCHES")
    elif min(cur_matches.keys()) == 0:
        results.append(cur_matches[0][0])
    else:
        min_wildcards = min(cur_matches.keys())
        best_match = get_best_match(cur_matches[min_wildcards], 0, "*")
        results.append(best_match)
        
    return results
    
def get_best_match(matches, start_index, target):
    if len(matches) == 1:
        return matches[0]
    
    cur_matches = matches
    
    left = cur_matches[0].index(target)
    result = {}
    
    for i in range (0, len(cur_matches)):
        if cur_matches[i][start_index:].index("*") >= left:
            left = cur_matches[i][start_index:].index("*")
            if left in result and cur_matches[i] not in result[left]:
                result[left].append(cur_matches[i])
            else:
                result[left] = [cur_matches[i]]
        
    if len(result[left]) > 1:
        return get_best_match(result[left], left + 1, "*")
    else:
        return result[left][0]
    
    # x = ((m.index("*"), m) for m in cur_matches)
    # print(max(((m.index("*"), m) for m in cur_matches))[1])
        
    # best_match = max(((m.index("*"), m) for m in cur_matches))[1]
    # return best_match

# don't need num_patterns or num_paths here
def get_matching_patterns(patterns, paths):
    
    #edge cases first
    
    results = []
    delimiter = ','
    
    for i, p in enumerate(paths): # might not need i 
        # remove leading and trailing /
        if p[0] == '/' or p[-1] == '/':
            p = p.strip('/')
            
        pathArr = p.split('/')
        
        matches = {} # dict O(1) lookup and insertion time
        
        for j, pattern in enumerate(patterns):
            patternArr = pattern.split(',')
            
            if len(patternArr) == len(pathArr):
                cur_pos = 0
                cur_match = [] # change name
                
                wildcard_count = 0 # will use wildcard count as key in matches dict
                
                while cur_pos < len(patternArr):
                    if patternArr[cur_pos] == "*":
                        cur_match += patternArr[cur_pos]
                        wildcard_count += 1
                        # cur_pos += 1
                    elif patternArr[cur_pos] == pathArr[cur_pos]:
                        cur_match.append(patternArr[cur_pos])
                        # cur_pos += 1
                    else:
                        # might move where this is invoked
                        # results.append("NO MATCHES")
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

    
# get_matching_patterns(len(patterns), patterns, len(paths), paths)