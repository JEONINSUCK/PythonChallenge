def Test(index):
    temp2 = ""
    for k in (len(index)):
        if index[k]!=index[k+1]:
            return index
        temp2 += index[k]
AntArray = [[0]for k in range(30)]              # 개미수열을 저장할 리스트 30칸을 만든다
AntArray[0] = "1"                               # 개미수열의 초기 값을 준다
print(AntArray)
for i in range(len(AntArray)):                  # 리스트의 값을 한개씩 가져와 계산을 하기전에 세팅
    index = AntArray[i]
    temp = ""
    for j in range(0,len(index)):               # 배열의 각 자리의 개수를 새어서 temp 변수에 개수+값의 형태로 문자화
        Test()
        count = index.count(index[j])           # 각배열의 값의 개수를 센다.
        temp += (str(count)+str(index[j]))      # 개수와 값을 하나씩 합쳐서 문자열을 만든다.

    AntArray[i+1] = temp                        # 완성된 문자열을 다음 배열에 할당.

print(AntArray)