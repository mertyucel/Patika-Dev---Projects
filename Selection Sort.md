## Insertion Short
### [22,27,16,2,18,6]

Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

Big-O gösterimini yazınız.

Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız

1. Average case: Aradığımız sayının ortada olması
2. Worst case: Aradığımız sayının sonda olması
3. Best case: Aradığımız sayının dizinin en başında olması.

## Sonuç

key = 1 den başlayarak devam ediyoruz.

[22,`27,16`,2,18,6] 

[`22,16`,27,2,18,6] 

[16,22,`27,2`,18,6] 

[16,`22,2`,27,18,6] 

[`16,2`,22,27,18,6] 

[2,16,22,`27,18`,6] 

[2,16,`22,18`,27,6] 

[2,16,18,22,`27,6`] 

[2,16,18,`22,6`,27] 

[2,16,`18,6`,22,27] 

[2,`16,6`,18,22,27] 

[`2,6,16,18,22,27`]


Insertion Sort’un time complexity’si :

- Best Case : O(n)
- Worst Case : O(n²)
- Average Case : O(n²)


18 sayısı `average case` kapsamına girer.

## Selection Short
### [7,3,5,8,2,9,4,15,6]  dizisinin Selection Sort'a göre ilk 4 adımını yazınız.

## Sonuç

1.[2,3,5,8,7,9,4,15,6]
2.[2,3,4,8,7,9,5,15,6]
3.[2,3,4,5,7,9,8,15,6]
4.[2,3,4,5,6,9,8,15,7]
