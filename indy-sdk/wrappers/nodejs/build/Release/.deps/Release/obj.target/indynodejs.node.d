cmd_Release/obj.target/indynodejs.node := g++ -o Release/obj.target/indynodejs.node -shared -pthread -rdynamic -m64  -Wl,-soname=indynodejs.node -Wl,--start-group Release/obj.target/indynodejs/src/indy.o -Wl,--end-group -L/home/fdiarra/workspace/indy-sdk/wrappers/nodejs -lindy