/*************************************************************************
	> File Name: bianliang.c
	> Author: case
	> Mail: qcypggs@qq.com
	> Created Time: 2018年07月25日 星期三 23时21分33秒
 ************************************************************************/
#include <stdio.h>
 
// 变量声明
extern int a, b;
extern int c;
extern float f;
 
int main ()
{
  /* 变量定义 */
  int a, b;
  int c;
  float f;
 
  /* 初始化 */
  a = 10;
  b = 20;
  
  c = a + b;
  printf("value of c : %d \n", c);
 
  f = 70.0/3.0;
  printf("value of f : %f \n", f);
 
  return 0;
}
