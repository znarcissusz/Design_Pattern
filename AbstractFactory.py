from abc import ABCMeta,abstractmethod

class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass

class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass

class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

class SmallShell(PhoneShell):
    def show_shell(self):
        print("SmallShell")

class BigShell(PhoneShell):
    def show_shell(self):
        print('BigShell')

class AppleShell(PhoneShell):
    def show_shell(self):
        print('AppleShell')

class SnapDragonCPU(CPU):
    def show_cpu(self):
        print('SnapDragonCPU')

class MediaTekCPU(CPU):
    def show_cpu(self):
        print('MediaTekCPU')

class AppleCPU(CPU):
    def show_cpu(self):
        print('AppleCPU')

class Android(OS):
    def show_os(self):
        print("Android_os")

class IOS(OS):
    def show_os(self):
        print('IOS')

class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragonCPU()
    def make_os(self):
        return Android()
    def make_shell(self):
        return BigShell()
#pay attention fix B b sensitive vim-lsp
class HuaweiFactory(PhoneFactory):
    def make_cpu(self):
        return MediaTekCPU()
    def make_os(self):
        return Android()
    def make_shell(self):
        return SmallShell()

class IPhoneFactory(PhoneShell):
    def make_cpu(self):
        return IOS()
    def make_cpu(self):
        return AppleCPU(self)
    def make_shell(self):
        return AppleShell()

class Phone:
    def __init__(self,cpu,os,shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print('cellphone_info:')
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()

def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu,os,shell)

p1 = make_phone(MiFactory())
p1.show_info()
