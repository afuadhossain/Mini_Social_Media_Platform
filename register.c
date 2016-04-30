#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void unencode(char *src, char *dest) {
    for(; *src != '\0'; src++, dest++) {
        if(*src == '+') {
            *dest = ' ';
        } else if(*src == '%') {
            char code;
            if(sscanf(src+1, "%2x", &code) != 1) code = '?';
            *dest = code;
            src += 2;
        } else {
            *dest = *src;
        }
    }
    *dest = '\0';
}

int main(void) {
    printf("Content-type:text/html\n\n");
    printf("<html><head><title>Registration</title></head><body>");

    char encodedBuffer[501];
    char username[21];
    char password[21];
    char fullname[51];
    char jobdesc[101];
    fgets(encodedBuffer,500,stdin);

    char buffer[501];
    unencode(encodedBuffer,buffer);

    char *p = buffer;
    int i = 0;
    while(*p!='=') p++;
    p++;
    while(*p!='&') {
        if(!isalpha(*p) && !isdigit(*p)) {
            printf("Invalid character in username. All characters must be alphanumeric!<br>");
            printf("<a href=\"http://cs.mcgill.ca/~ahossa6/ass4/welcome.html\">Back to landing page</a><br>");
            printf("<a href=\"http://cs.mcgill.ca/~hlee168/ass4/login.html\">Back to login page</a>");
            printf("</body></html>");
            return 0;
        }
        username[i] = *p;
        i++;
        p++;
    }
    username[i] = '\0';

    i = 0;
    while(*p!='=') p++;
    p++;
    while(*p!='&') {
        password[i] = *p;
        i++;
        p++;
    }
    password[i] = '\0';

    i = 0;
    while(*p!='=') p++;
    p++;
    while(*p!='&') {
        fullname[i] = *p;
        i++;
        p++;
    }
    fullname[i] = '\0';

    i = 0;
    while(*p!='=') p++;
    p++;
    while(*p!='&' && *p!='\0') {
        jobdesc[i] = *p;
        i++;
        p++;
    }
    jobdesc[i] = '\0';
    
    if(username[0]=='\0') {
        printf("Please enter a username.");
        printf("<a href=\"http://cs.mcgill.ca/~ahossa6/ass4/welcome.html\">Back to landing page</    a><br>");
        printf("<a href=\"http://cs.mcgill.ca/~ahossa6/ass4/login.html\">Back to login page</a>");
        printf("</body></html>");
        return 0;
    }
    if(password[0]=='\0') {
        printf("Please enter a password.");
        printf("<a href=\"http://cs.mcgill.ca/~ahossa6/ass4/welcome.html\">Back to landing page</    a><br>");
        printf("<a href=\"http://cs.mcgill.ca/~ahossa6/ass4/login.html\">Back to login page</a>");
        printf("</body></html>");
        return 0;
    }

    FILE *fp = fopen("/home/2015/hlee168/public_html/ass4/users.txt","a+");
    char buf[21];
    int line = 1;
    while(fgets(buf,20,fp)) {
        buf[strcspn(buf,"\n")] = 0;
        if(strcmp(buf,username)==0 && line%4==1) {
            printf("Username already exists.<br>");
            printf("<a href=\"http://cs.mcgill.ca/~ahossa6/ass4/welcome.html\">Back to landing page</a><br>");
            printf("<a href=\"http://cs.mcgill.ca/~ahossa6/ass4/login.html\">Back to login page</a>");
            printf("</body></html>");
            return 0;
        }
	line++;
    }
    fputs(username,fp);
    fputs("\n",fp);
    fputs(password,fp);
    fputs("\n",fp);
    fputs(fullname,fp);
    fputs("\n",fp);
    fputs(jobdesc,fp);
    fputs("\n",fp);
    fclose(fp);

    fp = fopen("/home/2015/hlee168/public_html/ass4/friends.txt","a");
    fprintf(fp,"%s\n",username);
    fclose(fp);
    
    printf("Registration successful!<br>");
    printf("Would you like to <a href=\"http://cs.mcgill.ca/~ahossa6/ass4/login.html\">login?</a>");
    printf("</body></html>");

    return 0;
}
