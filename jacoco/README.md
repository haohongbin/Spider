# 插桩配置
## jacoco 下载
下载地址：https://www.eclemma.org/jacoco/  
解压之后，lib/jacocoagent.jar 就是启动应用时主要用来插桩的 jar 包  
## 使用
### jar包方式启动
在 java -jar 启动的时候，加入-javaagent 参数  
```
-javaagent:/home/admin/jacoco/jacocoagent.jar=includes=*,output=tcpserver,port=2022,address=10.111.11.19

参数解释：
-javaagent：jdk5 之后新增的参数，主要用来在运行 jar 包的时候，以一种方式介入字节码加载过程
/home/admin/jacoco/jacocoagent.jar：需要用来介入 class 文件加载过程的 jar 包，是jar包的绝对路径
includes=*：这个代表了，启动时需要进行字节码插桩的包过滤，* 代表所有的 class 文件加载都需要进行插桩。如果有过滤可以写成：includes=com.task.*
output=tcpserver：这个地方不用改动，代表以 tcpserver 方式启动应用并进行插桩
port=2022：这是 jacoco 开启的 tcpserver 的端口，请注意这个端口不能被占用
address=10.111.11.19：这是对外开发的 tcpserver 的访问地址。可以配置 127.0.0.1,也可以配置为实际访问 ip
                      配置为 127.0.0.1 的时候，dump 数据只能在这台服务器上进行 dump，就不能通过远程方式 dump 数据。
                      配置为实际的 ip 地址的时候，就可以在任意一台机器上 (前提是 ip 要通)，通过 ant xml 或者 api 方式 dump 数据。
```
#### 命令
```
java -javaagent: $jacocoJarPath=includes=*,output=tcpserver,port=2022,address=10.111.11.19 -jar  xxxxxxxxxx.jar
注意，javaagent 参数，一定要在 jar 包路径之前，尽量在-jar 之前，不然可能不会生效。
```



ant dump时，如果报错Could not load definitions from resource org/jacoco/ant/antlib.xml
需要将jacoco中的jacocoant.jar包放到ant/lib目录下