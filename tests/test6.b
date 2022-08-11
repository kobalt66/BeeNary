start:
    :src<"[CURRDIR]/libs/math.b">:

#    flyout add<1, add<sub<2, 2>, 2>>
#
#    a honey add<2.3, 2.7>
#    b honey sub<7.5, 1.5>
#    c honey div<9, 3>
#    d honey mul<5, 5>
#    E honey pow<2, 2>
#    
#    flyout a 
#    flyout b 
#    flyout c 
#    flyout d
#    flyout E
#    
#    count honey 0
#    ee honey 2
# loop:
#     
#     ee honey pow<2, count>
#     flyout ee
#     
#     inv count is not 100 count honey add<count, 1>
#     inv count is 100 flyto after
# 
#     flyto loop 
#
# after:
#    vec honey vec2<1, 2>
#    y honey vec<Y>
#    flyout y 
#
#    vec honey vec3<1, 2, 3>
#    flyout vec<Z>
#    
#    flyout int<tan<1.5596856728972892>>
#  
#    flyout_matrix<add_matrices<mat2X2<123, 234, 98, 1>, mat2X3<1, 2, 3, 4, 5, 6>>>

    :src<"[CURRDIR]/libs/std.b">:

#    inv read_input<> is "password" flyout "Logged in!"
#
#    path honey replace_str<"[CURRDIR]/test_file.txt", "[CURRDIR]", curr_dir<>>
#    
#    inv exists<path> is false create_file<path>
#    
#    write_file<path, "Test string!!\nasdfasdf">
#    flyout read_file<path>
#
#    inv exists<path> is true del_file<path>
#
#    create_dir<path>
#    del_dir<path>
#
#    flyout join_str<"Hello", " World">
#
#    create_file<path>
#
#    inv exists<path> is true del_file<path>
#    inv exists<path> is false create_file<path>
#
#    flyout replace_str<"[CURRDIR]/test.txt", "[CURRDIR]", curr_dir<>>
#
#    flyout int<read_input<>>

#    inv add<1, 1> is 2 flyout "Math works"
#    inv add<1, 1> is not 2 flyout "Math works"
#    other flyout_matrix<mat2X2_identity<>>

#    flyout add<add<add<111, 111>, add<111, 111>>, 1>
#    _list honey list<1, 2, 3, 4, 5, 6, "", 8, 9, 10>
#    flyout lengthof<_list>
#    a honey ""
#    flyout a

:end: