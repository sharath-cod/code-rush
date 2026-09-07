bool isPalindrome(int x) {

    int res=0;
    int l;
    while(x!=0)
    {
        l=x%10;
        x=x/10;
        res=(res*10)+l;

    }
    if(res==x)

{
    return true;
}
return false;

}
