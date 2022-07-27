start:
    :src<"[CURRDIR]/libs/math.b">:
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
#    vec honey vectwo<1, 2>
#    y honey vec<Y>
#    flyout y 
#
#    vec honey vecthree<1, 2, 3>
#    z honey vec<Z>
#    flyout z
#    
#    #divbyzero honey div<1, 0>
#
#    a honey tan<1.5596856728972892>
#    a honey int<a>
#    flyout a
#   
#    matA honey mat_twoXtwo<123, 234, 98, 1>
#    matB honey mat_twoXthree<1, 2, 3, 4, 5, 6>
#    res honey add_matrices<matA, matB>
#    flyout_matrix<res>
    :src<"[CURRDIR]/libs/std.b">:

    #input honey read_input<>
    #inv input is "password" flyout "Logged in!"

    cwd honey curr_dir<>
    path honey "[CURRDIR]/test_file.txt"
    path honey replace_str<path, "[CURRDIR]", cwd>
    
    file_exists honey exists<path>
    inv file_exists is true flyto after
    create_file<path>
    after:
    
    write_file<path, "Test string!!\nasdfasdf">
    data honey read_file<path>
    flyout data

    del_file<path>
    file_exists honey exists<path>
    inv file_exists is false flyout "Deleted file"

    create_dir<path>
    del_dir<path>
    
:end: