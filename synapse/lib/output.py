'''
Tools for easily hookable output from cli-like tools.
'''
import synapse.compat as s_compat

class OutPut:

    def __init__(self):
        pass

    def printf(self, mesg, **args):
        if args:
            mesg = mesg % args

        return self._rawOutPut(mesg+'\n')

    def _rawOutPut(self, mesg):
        print( mesg[:-1] )

class OutPutFd(OutPut):

    def __init__(self, fd, enc='utf8'):
        OutPut.__init__(self)
        self.fd = fd
        self.enc = enc

    def _rawOutPut(self, mesg):
        self.fd.write(mesg.encode(self.enc))

class OutPutBytes(OutPutFd):

    def __init__(self):
        OutPutFd.__init__(self, s_compat.BytesIO())

class OutPutStr(OutPut):

    def __init__(self):
        OutPut.__init__(self)
        self.mesgs = []

    def _rawOutPut(self, mesg):
        self.mesgs.append(mesg)

    def __str__(self):
        return ''.join(self.mesgs)

#class OutPutBus(OutPut,EventBus):
    #def __init__(self, bus):
        #OutPut.__init__(self)
        #EventBus.__init__(self)

    #def _rawOutPut(self, mesg):
        #self.fire('output:print', mesg=mesg)

