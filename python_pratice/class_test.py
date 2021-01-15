class ClassTest :
    class_v = 10 # 클래스 변수 : 클래스 타입의 모든 instance 공유하는 변수 => 반드시 클래스 이름으로 참조해야 한다.

    def __init__(self, instance_v) :
        self.instance_v = instance_v

c1 = ClassTest(10)
c2 = ClassTest(10)

c1.instance_v += 1
c2.instance_v += 1
print("c1.instance_v : {0}, c2.instance_v : {1}".format(c1.instance_v, c2.instance_v))

ClassTest.class_v += 1
c1.class_v += 1
print("c1.class_v : {0}".format(c1.class_v))

ClassTest.class_v += 1
print("c1.class_v : {0}".format(ClassTest.class_v))