/*************************************************************************
	> File Name: ifelse.c
	> Author: case
	> Mail: qcypggs@qq.com
	> Created Time: 2018年07月25日 星期三 23时27分37秒
 ************************************************************************/
#include <stdio.h>
 
int main ()
{
   /* 局部变量定义 */
   int a = 100;
 
   /* 检查布尔条件 */
   if( a < 20 )
   {
       /* 如果条件为真，则输出下面的语句 */
       printf("a 小于 20\n" );
   }
   else
   {
       /* 如果条件为假，则输出下面的语句 */
       printf("a 大于 20\n" );
   }
   printf("a 的值是 %d\n", a);
 
   return 0;
}
