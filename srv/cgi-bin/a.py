from casl import*
def a(a,b=0):return a
class A:
  def getElementById(a):return{"style":{}}
  def getElementsByTagName(a):return{}
casl.document=A
class B:
  class C:
    document=A
    scrollTo=a
  conframe=C
  progframe=C
casl.top=B
casl.lineHeight=13
casl.spInit=65535
casl.formatSourceLine=a
casl.enCER=a
casl.inputRegMem=a
casl.outputRegMem=a
casl.alert=a
ret=["A START"," DC #1210,#7,#1220,#8,#F000,#2,#8100,#41,#1"," END"]
casl.assemble(ret,0,0,0)
casl.setState(2)
casl.initializeRegMem()
casl.go()
ret=casl.consoleView.arrayLines[0]
print("content-type:text/html\n\n"+ret)