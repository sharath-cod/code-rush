bool isPalindrome(char* s)
 {
    int i=0;
    int j=strlen(s);
    while(i>j)
    {
        if(!isalnum(s[i]))
        {
            i++;
            
        }
        if(!isalnum(s[j]))
        {
            j--;
        }
        if(tolower(s[i]) != tolower(s[j]))
            return false;
            i++;
            j--;
        
        
    }
return true;

}
