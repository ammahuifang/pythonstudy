#��ҵ3���ð�����ɫ��ɸ���0-n��������list
'''
������ɫ��ɸѡ��(the Sieve of Eratosthenes)��ư���ɸ����
�ǹ�ϣ����ѧ�Ұ�����ɫ��(Eratosthenes 274B.C.��194B.C.)�����һ��ɸѡ����
�������Ȼ�����е���Ȼ����ʵʩ�ģ�������һ����Χ�ڵ������������ݳ�ԭ��֮�걸��������p=H~��
'''

def _int_iter():
    n=1
    while True:
        n=n+1
        yield n
def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    it=_int_iter()
    while True:
    
