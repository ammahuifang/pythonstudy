#��ҵ1����дһ���������õݹ�ķ������쳲�������(Fibonacci sequence)����list
'''
�ݹ麯��
�ں����ڲ������Ե����������������һ���������ڲ���������������������ǵݹ麯����
�ٸ����ӣ�����������׳� n! = 1 * 2 * 3 * ... * n���ú��� fact(n)��ʾ�����Կ�����
fact(n) = n! = 1 * 2 * 3 * ... * (n-1) * n = (n-1)! * n = fact(n-1) * n
���ԣ�fact(n)���Ա�ʾΪ n * fact(n-1)��ֻ��n=1ʱ��Ҫ���⴦��
���ǣ�fact(n)�õݹ�ķ�ʽд�������ǣ�


def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
'''

x=int(input("����һ������"))
def fib(n):   
    if n==0:
        return 0
    if n==1:
        return 1    
    return fib(n-1)+fib(n-2)
for i in range(1,x+1):
    print(fib(i))


'''
����һ������6
1
1
2
3
5
8
'''
