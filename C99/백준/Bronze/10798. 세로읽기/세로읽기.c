#include <stdio.h>

int main(){
    char arr[5][15];
    int i, len[5], maxlen;
    
    for(i=0;i<5;i++){
        gets(arr[i]);
        len[i]=strlen(arr[i]);
        if(maxlen<len[i])maxlen=len[i];
    }
    int sumlen=0;
    for(i=0;i<5;i++) sumlen+=len[i];
    
   for(i=0;i<maxlen;i++){
        for(int j=0;j<5;j++){
            if(len[j]>0) printf("%c",arr[j][i]);
            len[j]--;
        }
    }
}