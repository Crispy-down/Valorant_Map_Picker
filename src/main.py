from tkinter import *
import os
import sys
import tkinter.messagebox as msgbox

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

root = Tk() # root를 통해 Tk 선언

pos = -1
proc = ""
progress_str = [ 
                "RED TEAM BAN PICK",
                "BLUE TEAM BAN PICK" ,
                "RED TEAM FIRST MAP PICK",
                "BLUE TEAM SELECT SIDE" ,
                "BLUE TEAM FIRST MAP PICK",
                "RED TEAM SELECT SIDE" ,
                "RED TEAM SECOND BAN PICK",
                "BLUE TEAM SECOND BAN PICK",
                "RED TEAM LAST MAP SELECT SIDE " ] # idx 8 (9단계)

Map_Ban_Status = [0,0,0,0,0,0,0] # 맵 밴픽 상태 
Map_call = ["Ascent","Fracture","Haven","Icebox","Lotus","Pearl","Split"]
# ASCENT / FRACTURE / HAVEN / ICEBOX / LOTUS / PEARL / SPLIT
# 0 = remain / 1 = Pick / -1 = ban


Map_Set1_map = " "
Map_Set1_A_side = StringVar()
Map_Set1_A_side.set("")
Map_Set1_B_side = StringVar()
Map_Set1_B_side.set("")

Map_Set2_map = " "
Map_Set2_A_side = StringVar()
Map_Set2_A_side.set("")
Map_Set2_B_side = StringVar()
Map_Set2_B_side.set("")

Map_Set3_map = " "
Map_Set3_A_side = StringVar()
Map_Set3_A_side.set("")
Map_Set3_B_side = StringVar()
Map_Set3_B_side.set("")
# 맵 / A 사이드 / B 사이드 ex. Icebox , ATT , DEF

#####################################################################################

p1 = PhotoImage(file = resource_path("val.png")) # 아이콘 설정
bg = PhotoImage(file = resource_path("bg_3.png"))

Split = PhotoImage(file = resource_path("Split_normal.png")) # 맵
Haven = PhotoImage(file = resource_path("Haven_normal.png")) # 맵
Ascent = PhotoImage(file = resource_path("Ascent_normal.png")) # 맵
Icebox = PhotoImage(file = resource_path("Icebox_normal.png")) # 맵
Fracture = PhotoImage(file = resource_path("Fracture_normal.png")) # 맵
Pearl = PhotoImage(file = resource_path("Pearl_normal.png")) # 맵
Lotus = PhotoImage(file = resource_path("Lotus_normal.png")) # 맵


Split_ban = PhotoImage(file = resource_path("Split_ban.png")) # 맵
Haven_ban = PhotoImage(file = resource_path("Haven_ban.png")) # 맵
Ascent_ban = PhotoImage(file = resource_path("Ascent_ban.png")) # 맵
Icebox_ban = PhotoImage(file = resource_path("Icebox_ban.png")) # 맵
Fracture_ban = PhotoImage(file = resource_path("Fracture_ban.png")) # 맵
Pearl_ban = PhotoImage(file = resource_path("Pearl_ban.png")) # 맵
Lotus_ban = PhotoImage(file = resource_path("Lotus_ban.png")) # 맵

Split_pick = PhotoImage(file = resource_path("Split_pick.png")) # 맵
Haven_pick = PhotoImage(file = resource_path("Haven_pick.png")) # 맵
Ascent_pick = PhotoImage(file = resource_path("Ascent_pick.png")) # 맵
Icebox_pick = PhotoImage(file = resource_path("Icebox_pick.png")) # 맵
Fracture_pick = PhotoImage(file = resource_path("Fracture_pick.png")) # 맵
Pearl_pick = PhotoImage(file = resource_path("Pearl_pick.png")) # 맵
Lotus_pick = PhotoImage(file = resource_path("Lotus_pick.png")) # 맵

Att_button = PhotoImage(file = resource_path("ATK_bg.png")) 
Def_button = PhotoImage(file =  resource_path("DEF_bg.png"))

Split_Set = PhotoImage(file =  resource_path("split_set.png")) # 맵 7번 
Haven_Set = PhotoImage(file = resource_path("haven_set.png")) # 맵
Ascent_Set = PhotoImage(file = resource_path("ascent_set.png")) # 맵
Icebox_Set = PhotoImage(file = resource_path("icebox_set.png")) # 맵
Fracture_Set = PhotoImage(file = resource_path("fracture_set.png")) # 맵
Pearl_Set = PhotoImage(file = resource_path("pearl_set.png")) # 맵
Lotus_Set = PhotoImage(file = resource_path("lotus_set.png")) # 맵

Gc_red = PhotoImage(file = resource_path("Red_team.png"))
Gc_blue = PhotoImage(file = resource_path("Blue_team.png"))

Unknown_map = PhotoImage(file = resource_path("unknown.png"))


#####################################################################################

bg_label = Label(root,image = bg)
bg_label.place(x = -2, y = -2)

root.title("Valorant Map Pick") # 창 제목
root.geometry("1366x768") # 창 크기
root.resizable(False, False) # 창 크기 조절 허용 x
root.iconphoto(False, p1) # 창 아이콘 변경

#####################################################################################
    
def last_map_update(): # 선정되거나 밴되지 않은 마지막 맵
    # 맵 인자 리턴
    for i in range(len(Map_Ban_Status)):
        if(Map_Ban_Status[i] == 0):
            return i
        
def img_ban_pick(idx): # 밴픽 이미지 변경 함수
    if(idx == 0):
        Map_Ascent.configure(image = Ascent_ban)
    elif(idx == 1):
        Map_Fracture.configure(image = Fracture_ban)
    elif(idx == 2):
        Map_Haven.configure(image = Haven_ban)
    elif(idx == 3):
        Map_Icebox.configure(image = Icebox_ban)
    elif(idx == 4):
        Map_Lotus.configure(image = Lotus_ban)
    elif(idx == 5):
        Map_Pearl.configure(image = Pearl_ban)
    elif(idx == 6):
        Map_Split.configure(image = Split_ban)

def img_sel_pick(idx): #선정 픽 이미지 변경 함수
    if(idx == 0):
        Map_Ascent.configure(image = Ascent_pick)
    elif(idx == 1):
        Map_Fracture.configure(image = Fracture_pick)
    elif(idx == 2):
        Map_Haven.configure(image = Haven_pick)
    elif(idx == 3):
        Map_Icebox.configure(image = Icebox_pick)
    elif(idx == 4):
        Map_Lotus.configure(image = Lotus_pick)
    elif(idx == 5):
        Map_Pearl.configure(image = Pearl_pick)
    elif(idx == 6):
        Map_Split.configure(image = Split_pick)
        
def first_set_map(idx):
    if(idx == 0):
        Map_Set_1_map.configure(image = Ascent_Set)
    elif(idx == 1):
        Map_Set_1_map.configure(image = Fracture_Set)
    elif(idx == 2):
        Map_Set_1_map.configure(image = Haven_Set)
    elif(idx == 3):
        Map_Set_1_map.configure(image = Icebox_Set)
    elif(idx == 4):
        Map_Set_1_map.configure(image = Lotus_Set)
    elif(idx == 5):
        Map_Set_1_map.configure(image = Pearl_Set)
    elif(idx == 6):
        Map_Set_1_map.configure(image = Split_Set)

def second_set_map(idx):
    if(idx == 0):
        Map_Set_2_map.configure(image = Ascent_Set)
    elif(idx == 1):
        Map_Set_2_map.configure(image = Fracture_Set)
    elif(idx == 2):
        Map_Set_2_map.configure(image = Haven_Set)
    elif(idx == 3):
        Map_Set_2_map.configure(image = Icebox_Set)
    elif(idx == 4):
        Map_Set_2_map.configure(image = Lotus_Set)
    elif(idx == 5):
        Map_Set_2_map.configure(image = Pearl_Set)
    elif(idx == 6):
        Map_Set_2_map.configure(image = Split_Set)
    
def third_set_map(idx):
    if(idx == 0):
        Map_Set_3_map.configure(image = Ascent_Set)
    elif(idx == 1):
        Map_Set_3_map.configure(image = Fracture_Set)
    elif(idx == 2):
        Map_Set_3_map.configure(image = Haven_Set)
    elif(idx == 3):
        Map_Set_3_map.configure(image = Icebox_Set)
    elif(idx == 4):
        Map_Set_3_map.configure(image = Lotus_Set)
    elif(idx == 5):
        Map_Set_3_map.configure(image = Pearl_Set)
    elif(idx == 6):
        Map_Set_3_map.configure(image = Split_Set)
    
    

def map_select(map_idx) : # 맵 클릭시 실행되는 함수, 클릭시 어떤 맵인지 받아와야함
    global pos
    global Map_Set1_map
    global Map_Set2_map
    global Map_Set3_map
    
    
    if(pos == 0): # A 밴픽
        if(Map_Ban_Status[map_idx] == 0): #이미 선정했거나 밴한 맵 다시 변경 금지 (선정안된 맵만 밴/ 선정 가능)
            Map_Ban_Status[map_idx] = -1
            img_ban_pick(map_idx) # 이미지 변경    
            # 맵 흑백 사진 대체
    elif(pos == 1): # B 밴픽
        if(Map_Ban_Status[map_idx] == 0):
            Map_Ban_Status[map_idx] = -1
            img_ban_pick(map_idx) # 이미지 변경   
            # 맵 흑백 사진 대체
    elif(pos == 2): # A 픽
        if(Map_Ban_Status[map_idx] == 0):
            Map_Ban_Status[map_idx] = 1
            img_sel_pick(map_idx) # 이미지 변경  
            first_set_map(map_idx)
            Map_Set1_map = Map_call[map_idx] # Set1 Map 업데이트
            Map_Set_1_name.configure(text=Map_Set1_map) 
            # 맵 PICK 사진 대체
    elif(pos == 4): # B 픽
        if(Map_Ban_Status[map_idx] == 0):
            Map_Ban_Status[map_idx] = 1
            img_sel_pick(map_idx) # 이미지 변경 
            second_set_map(map_idx)
            Map_Set2_map = Map_call[map_idx] # Set2 Map 업데이트
            Map_Set_2_name.configure(text=Map_Set2_map)  
            # 맵 PICK 사진 대체
    elif(pos == 6): # A 밴픽
        if(Map_Ban_Status[map_idx] == 0):
            Map_Ban_Status[map_idx] = -1
            img_ban_pick(map_idx) # 이미지 변경   
            # 맵 흑백 사진 대체
    elif(pos == 7): # B 밴픽
        if(Map_Ban_Status[map_idx] == 0):
            Map_Ban_Status[map_idx] = -1
            img_ban_pick(map_idx) # 이미지 변경   
            # 맵 흑백 사진 대체
            img_sel_pick(last_map_update()) # 라스트 맵 선정
            third_set_map(last_map_update())
            Map_Set3_map = Map_call[last_map_update()] # 마지막 남은 맵 업데이트
            Map_Set_3_name.configure(text=Map_Set3_map)
            # 맵 PICK 사진 대체
    else:
        msgbox.showwarning("경고","맵 선정 차례가 아닙니다")

        

def map_side_select(side): # 공수 버튼 선택시 실행되는 함수
    # ATT or DEF
    global pos
    global Map_Set1_A_side
    global Map_Set1_B_side
    global Map_Set2_A_side
    global Map_Set2_B_side
    global Map_Set3_A_side
    global Map_Set3_B_side
    
    if(side == "ATT"): 
        alter_side = "DEF"
    else:
        alter_side = "ATT"
        
    if(pos == 3): # B팀 set 1 공수선정
        Map_Set_1_side_A.configure(text = "Red Team: " + alter_side)
        Map_Set_1_side_B.configure(text = "Blue Team: " + side)
    elif(pos == 5): # A팀 set 2 공수선정
        Map_Set_2_side_A.configure(text = "Red Team: " + side)
        Map_Set_2_side_B.configure(text = "Blue Team: " + alter_side)
    elif(pos == 8):
        Map_Set_3_side_A.configure(text = "Red Team: " + side)
        Map_Set_3_side_B.configure(text = "Blue Team: " + alter_side)
    else:
        msgbox.showwarning("경고","공수선정 차례가 아닙니다")
        


def btnnext(event) : # 다음 단계 넘어가는 함수 -> 여기서 다 함수 콜링 (main)
    global pos, proc
    pos += 1 
    if(pos > 8):
        msgbox.showinfo("프로그램 종료","Set 1 : " + Map_Set1_map + "\nSet 2 : " + Map_Set2_map + "\nSet 3 : " + Map_Set3_map)
        return 
    
    proc = progress_str[pos]
    process.config(text = proc)
    
    if(pos == 0):     
        msgbox.showinfo("정보","팀 A 첫번째 밴 픽 차례입니다.")
    elif(pos == 1):
        msgbox.showinfo("정보","팀 B 첫번째 밴 픽 차례입니다.")
    elif(pos == 2):
        msgbox.showinfo("정보","팀 A 1세트 맵 픽 차례입니다.")
    elif(pos == 3):
        msgbox.showinfo("정보","팀 B 1세트 공수 선정 차례입니다.")
    elif(pos == 4):
        msgbox.showinfo("정보","팀 B 2세트 맵 픽 차례입니다.")
    elif(pos == 5):
        msgbox.showinfo("정보","팀 A 2세트 공수 선정 차례입니다.")
    elif(pos == 6):
        msgbox.showinfo("정보","팀 A 두번째 밴 픽 차례입니다.")
    elif(pos == 7):
        msgbox.showinfo("정보","팀 B 두번째 밴 픽 차례입니다.")
    elif(pos == 8):
        msgbox.showinfo("정보","팀 A 3세트 공수 선정 차례입니다.")

    
#####################################################################################

process_bar = Frame(root,relief = "solid", bd=1, bg = "#0f1923", highlightbackground='white', highlightthickness=2) #1번 컴포넌트
process_bar.place(x = 20 , y = 16 , width=1330, height=104)
process_bar.bind("<Button-1>", btnnext) # frame (label 피해서) 누르면 상태 전환

Team_A = Frame(root, relief = "solid", bd = 1 , bg = "white") #2번 컴포넌트
Team_A.place(x=20, y = 138, width=324 , height=100)

Side_Att = Frame(root, relief = "solid", bd = 1, bg = "white") #3번 컴포넌트
Side_Att.place(x = 435, y = 158, width=200, height=80)

Side_Def = Frame(root, relief = "solid", bd = 1, bg = "white") #4번 컴포넌트
Side_Def.place(x = 730, y = 158, width=200, height= 80)

Team_B = Frame(root, relief = "solid", bd = 1, bg = "white") #5번 컴포넌트
Team_B.place(x = 1026, y = 138, width=324, height=100)

Map_Selector = Frame(root, relief="solid", bd = 1, bg = "#0f1923", highlightbackground='white', highlightthickness=2) #6번 컴포넌트
Map_Selector.place(x = 16, y = 272, width=1334, height=280)

Map_Set_1 = Frame(root, relief="solid", bd = 1, bg = '#0f1923', highlightbackground='white', highlightthickness=2) #7번 컴포넌트
Map_Set_1.place(x = 16, y = 572, width=420, height=180)

Map_Set_2 = Frame(root, relief="solid", bd = 1, bg = '#0f1923', highlightbackground='white', highlightthickness=2) #7번 컴포넌트
Map_Set_2.place(x = 473, y = 572, width=420, height=180)

Map_Set_3 = Frame(root, relief="solid", bd = 1, bg = '#0f1923', highlightbackground='white', highlightthickness=2) #7번 컴포넌트
Map_Set_3.place(x = 930, y = 572, width=420, height=180)

#####################################################################################

process = Label(process_bar, text = "Click Here To Start", font = ("Arial", 50), bg = '#0f1923', fg = 'white') #1번 내용
process.pack(pady = 16) 

Team_A_img = Label(Team_A, image = Gc_red, bg = "white", bd = 1) #2번 사진
Team_A_img.pack(pady = 1, padx = 1)

Attack = Button(Side_Att, image = Att_button, font = ("Arial",50), bg = "white", command = lambda : map_side_select("ATT")) # 3번 내용
Attack.pack(fill = "both")

Defend = Button(Side_Def, image = Def_button, font = ("Arial",50), bg = "white", command = lambda : map_side_select("DEF")) # 4번 내용
Defend.pack(fill = "both")

Team_B_img = Label(Team_B, image = Gc_blue, bg = "white", bd = 1) #2번 사진
Team_B_img.pack(pady = 1, padx = 1)

Map_Ascent = Button(Map_Selector, image = Ascent, bg = '#0f1923', width=182, height=280, command=lambda : map_select(0)) #6번 컴포넌트 이미지 버튼
Map_Ascent.pack(side="left", padx= 1)

Map_Fracture = Button(Map_Selector, image = Fracture, bg = '#0f1923', width=182, height=280, command=lambda : map_select(1)) #6번 컴포넌트 이미지 버튼
Map_Fracture.pack(side="left", padx= 1)

Map_Haven = Button(Map_Selector, image = Haven, bg = '#0f1923', width=182, height=280, command=lambda : map_select(2)) #6번 컴포넌트 이미지 버튼
Map_Haven.pack(side="left", padx= 1) 

Map_Icebox = Button(Map_Selector, image = Icebox, bg = '#0f1923', width=182, height=280, command=lambda : map_select(3)) #6번 컴포넌트 이미지 버튼
Map_Icebox.pack(side="left", padx= 1)

Map_Lotus = Button(Map_Selector, image = Lotus, bg = '#0f1923', width=182, height=280, command=lambda : map_select(4)) #6번 컴포넌트 이미지 버튼
Map_Lotus.pack(side="left", padx= 1)

Map_Pearl = Button(Map_Selector, image = Pearl, bg = '#0f1923', width=182, height=280, command=lambda : map_select(5)) #6번 컴포넌트 이미지 버튼
Map_Pearl.pack(side="left", padx= 1)

Map_Split = Button(Map_Selector, image = Split, bg = '#0f1923', width=182, height=280, command=lambda : map_select(6)) #6번 컴포넌트 이미지 버튼
Map_Split.pack(side="left", padx= 1)


Map_Set_1_map = Label(Map_Set_1, image = Unknown_map, bd = 1, bg = '#0f1923', width=242, height=160) # 7번-1 Map Label
Map_Set_1_map.pack(fill = "y", side = "left")
Map_Set_1_set = Label(Map_Set_1, text = "SET 1", font = ("Arial",17), bd = 1, bg = '#0f1923', fg = 'white') #7번-1 Set Label
Map_Set_1_set.pack(side = "top", fill= "x", pady= 10)
Map_Set_1_name = Label(Map_Set_1, text = "", font = ("Arial 17 bold"), bd = 1, bg = '#0f1923', fg = 'white') #7번-1 Map Label
Map_Set_1_name.pack(side = "top", fill= "x", pady= 5)
Map_Set_1_side_A = Label(Map_Set_1, text = "Red Team: ", font = ("Arial", 15), bd = 1, bg = '#0f1923', fg = 'red') #7번-1 A Side
Map_Set_1_side_A.pack(side= "top", fill = "x", pady = 10)
Map_Set_1_side_B = Label(Map_Set_1, text = "Blue Team: ", font = ("Arial", 15), bd = 1, bg = '#0f1923', fg = 'blue') #7번-1 B Side
Map_Set_1_side_B.pack(side= "top", fill = "x")

Map_Set_2_map = Label(Map_Set_2, image = Unknown_map, bd = 1, bg = '#0f1923', width=242, height=160) # 7번-2 Map Label
Map_Set_2_map.pack(fill = "y", side = "left")
Map_Set_2_set = Label(Map_Set_2, text = "SET 2", font = ("Arial",17), bd = 1, bg = '#0f1923', fg = 'white') #7번-2 Set Label
Map_Set_2_set.pack(side = "top", fill= "x", pady= 10)
Map_Set_2_name = Label(Map_Set_2, text = "", font = ("Arial 17 bold"), bd = 1, bg = '#0f1923', fg = 'white') #7번-2 Set Label
Map_Set_2_name.pack(side = "top", fill= "x", pady= 5)
Map_Set_2_side_A = Label(Map_Set_2, text =  "Red Team: ", font = ("Arial", 15), bd = 1, bg = '#0f1923', fg = 'red') #7번-2 A Side
Map_Set_2_side_A.pack(side= "top", fill = "x", pady = 10)
Map_Set_2_side_B = Label(Map_Set_2, text = "Blue Team: ", font = ("Arial", 15), bd = 1, bg = '#0f1923', fg = 'blue') #7번-2 B Side
Map_Set_2_side_B.pack(side= "top", fill = "x")

Map_Set_3_map = Label(Map_Set_3, image = Unknown_map, bd = 1, bg = '#0f1923', width=242, height=160) # 7번-3 Map Label
Map_Set_3_map.pack(fill = "y", side = "left")
Map_Set_3_set = Label(Map_Set_3, text = "SET 3", font = ("Arial",17), bd = 1, bg = '#0f1923', fg = 'white') #7번-3 Set Label
Map_Set_3_set.pack(side = "top", fill= "x", pady= 10)
Map_Set_3_name = Label(Map_Set_3, text = "", font = ("Arial 17 bold"), bd = 1, bg = '#0f1923', fg = 'white') #7번-3 Set Label
Map_Set_3_name.pack(side = "top", fill= "x", pady= 5)
Map_Set_3_side_A = Label(Map_Set_3, text =  "Red Team: ", font = ("Arial", 15), bd = 1, bg = '#0f1923', fg = 'red') #7번-3 A Side
Map_Set_3_side_A.pack(side= "top", fill = "x", pady = 10)
Map_Set_3_side_B = Label(Map_Set_3, text = "Blue Team: ", font = ("Arial", 15), bd = 1, bg = '#0f1923', fg = 'blue') #7번-3 B Side
Map_Set_3_side_B.pack(side= "top", fill = "x")

# 가변문자열 사용해야할 듯??

#####################################################################################

root.mainloop() # 루트에 메인 루프 선언

#프레임 창이 종료버튼을 누르기 전까지 종료 x


