#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
int main(void) {
    printf("Content-Type:text/html\n\n");
    printf("<html><head>");
    char string[100];
    fgets(string,99,stdin);
    char username[21];
    char password[21];
    char *p = string;
    while(*p!='=') p++;
    p++;
    int i = 0;
    while(*p!='&') {
        username[i] = *p;
        i++;
        p++;
    }
    username[i]='\0';
    while(*p!='=') p++;
    p++;
    i = 0;
    while(*p!='\0') {
        password[i] = *p;
        i++;
        p++;
    }
    password[i]='\0';

    FILE *fp;
    fp = fopen("/home/2015/hlee168/public_html/ass4/users.txt","rt");
    int line = 1;
    char buffer[200];
    while(!feof(fp)) {
        fgets(buffer,199,fp);
        buffer[strcspn(buffer,"\n")] = 0;
        if(strcmp(buffer,username)==0 && line%4==1) {
            fgets(buffer,199,fp);
            buffer[strcspn(buffer,"\n")] = 0;
            if(strcmp(buffer,password)==0) {
                printf("<script>setTimeout(function() { document.forms[0].submit() },1000);</script>");
                printf("</head><body>Login successful! Redirecting you to the dashboard...<form action=\"http://cs.mcgill.ca/~mrosen51/ass4/dashboard.py\" method=\"post\"><input type=\"hidden\" name=\"username\" value=\"%s\"/></body></html>",username);
                return 0;
            } else {
                printf("Wrong password.<br>");
                printf("<a href=\"http://cs.mcgill.ca/~ahossa6/ass4/login.html\">Click here to head back to the login page</a>");
                printf("</body></html>");
                return 0;
            }
        }
        line++;
    }
    printf("The following username was not found in our database.<br>");
    printf("<a href=\"http://cs.mcgill.ca/~ahossa6/ass4/login.html\">Click here to head back to the login page</a>");
    printf("</body></html>");
    return 0;
}
