lesson_list = []


def reset():
    lesson_list.append(['基礎程式設計：使用Scratch 3.X', []])
    lesson_list[0][1].append(['基礎篇', []])
    #--------------------------------名稱-----,檔案下載,編號,官網作品編號, tab, Youtube
    lesson_list[0][1][0][1].append(['教材：貓狗對話', False, 1, 199354464, False, False])
    lesson_list[0][1][0][1].append(['習作：勇者鬥惡龍', False, 2, 199356271, False, False])    
    lesson_list[0][1].append(['計算篇', []])
    lesson_list[0][1][1][1].append(['教材：求平均數', False, 3, 201792802, ["流程圖", "2_1.png"], False])          
    lesson_list[0][1][1][1].append(['教材：成績計算', False, 4, 201793143, ["流程圖", "2_2.png"], False])     
    lesson_list[0][1][1][1].append(['教材：累加計算', False, 5, 201793794, ["流程圖", "2_3.png"], False])    
    lesson_list[0][1][1][1].append(['教材：累乘計算', False, 6, 201794048, ["流程圖", "2_4.png"], False])  
    lesson_list[0][1][1][1].append(['教材：密碼檢查', False, 7, 201794208, ["流程圖", "2_5.png"], False])    
    lesson_list[0][1][1][1].append(['習作：溫度換算', False, 8, 201792945, ["流程圖", "6_1.png"], False])
    lesson_list[0][1][1][1].append(['習作：書店打折', False, 9, 201793454, ["流程圖", "6_2.png"], False])                
    lesson_list[0][1].append(['繪圖篇', []])
    lesson_list[0][1][2][1].append(['教材：畫方形', False, 10, 201791759, False, False])       
    lesson_list[0][1][2][1].append(['教材：擴散方形', False, 11, 201792210, False, False])         
    lesson_list[0][1][2][1].append(['教材：旋轉方形', False, 12, 201792359, False, False])    
    lesson_list[0][1][2][1].append(['習作：畫星星', False, 13, 201791984, False, False])      
    lesson_list[0][1][2][1].append(['習作：放大方形', False, 14, 201792631, False, False])  
    lesson_list[0][1][2][1].append(['習作：平行方形', False, 15, 201792490, False, False])                 
    lesson_list[0][1].append(['遊戲篇', []])
    lesson_list[0][1][3][1].append(['教材：狗狗散步', False, 16, 212207324, ["心智圖", "4_1.png"], False])  
    lesson_list[0][1][3][1].append(['教材：賽馬', False, 17, 212208431, ["心智圖", "4_2.png"], False])  
    lesson_list[0][1][3][1].append(['教材：水族箱', False, 18, 290858812, ["心智圖", "4_3.png"], False])  
    lesson_list[0][1][3][1].append(['教材：大馬路', False, 19, 213986419, ["心智圖", "4_4.png"], False])      
    lesson_list[0][1][3][1].append(['教材：打擊魔鬼', "1_20.zip", 20, 213986594, ["心智圖", "4_5.png"], False])
    lesson_list[0][1][3][1].append(['習作：打地鼠', False, 21, 216179680, ["心智圖", "6_5.png"], False])  
    lesson_list[0][1][3][1].append(['習作：打雷', "1_22.zip", 22, 201575317, ["心智圖", "4_6.png"], False])            
    lesson_list[0][1].append(['模擬篇', []])
    lesson_list[0][1][4][1].append(['教材：電子琴', "1_23.zip", 23, 201575462, False, False])  
    lesson_list[0][1][4][1].append(['教材：電梯', "1_24.zip", 24, 201575481, False, False])
 
    lesson_list.append(['進階程式設計：使用Scratch 3.X', []])
    lesson_list[1][1].append(['陣列篇', []])
    #--------------------------------名稱-----,檔案下載,編號,官網作品編號, tab, Youtube
    lesson_list[1][1][0][1].append(['教材：抽獎', False, 1, 292000745, False, False])
    lesson_list[1][1][0][1].append(['教材：所有因數', False, 2, 292001403, False, False])  
    lesson_list[1][1][0][1].append(['教材：發牌', "2_3.zip", 3, 292001972, False, False])    
    lesson_list[1][1][0][1].append(['習作：環保測驗', False, 4, 292666174, False, False])  
    lesson_list[1][1].append(['角色變數篇', []])
    lesson_list[1][1][1][1].append(['教材：戰車王', "2_5.zip", 5, 292002495, False, False])          
    lesson_list[1][1][1][1].append(['習作：星際大戰', "2_6.zip", 6, 292003017, False, False])                     
    lesson_list[1][1].append(['分身篇', []])
    lesson_list[1][1][2][1].append(['教材：螞蟻搬乳酪', "2_7.zip", 7, 292004483, False, False])       
    lesson_list[1][1][2][1].append(['教材：電子琴模擬', "2_8.zip", 8, 292659309, False, False])         
    lesson_list[1][1][2][1].append(['習作：水族箱', False, 9, 292657727, False, False])    
    lesson_list[1][1][2][1].append(['習作：打蚊子', "2_10.zip", 10, 292659400, False, False])                     
    lesson_list[1][1].append(['模組化篇', []])
    lesson_list[1][1][3][1].append(['教材：平行方形', False, 11, 292656980, False, False])  
    lesson_list[1][1][3][1].append(['教材：擴散方形', False, 12, 292657073, False, False])  
    lesson_list[1][1][3][1].append(['教材：小鳥吃蟲', "2_13.zip", 13, 292657280, False, False])  
    lesson_list[1][1][3][1].append(['習作：隨機畫星星', False, 14, 292657335, False, False])               
    lesson_list[1][1].append(['演算法篇', []])
    lesson_list[1][1][4][1].append(['教材：選擇排序法', False, 15, 292657387, False, False])  
    lesson_list[1][1][4][1].append(['教材：插入排序法', False, 16, 292657485, False, False])   
    lesson_list[1][1][4][1].append(['教材：循序搜尋法', False, 17, 292658576, False, False])   
    lesson_list[1][1][4][1].append(['教材：二元搜尋法', False, 18, 292658796, False, False]) 
    lesson_list[1][1].append(['附錄篇', []])
    lesson_list[1][1][5][1].append(['教材：跨欄比賽', "2_19.zip", 19, 375512447, False, False])  
    lesson_list[1][1][5][1].append(['教材：后羿射日', "2_20.zip", 20, 376829157, False, False])   
    lesson_list[1][1][5][1].append(['教材：蒙地卡羅法', False, 21, 359010095, False, False])   
reset()

