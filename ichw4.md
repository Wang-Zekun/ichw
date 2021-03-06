## 概论作业4
  
### Q1：解释作业、进程、线程的概念，进程和线程概念的提出分别解决了什么问题？  

- 作业：作业是用户向计算机提交的任务实体（用户要求计算机完成的任务集合），包括程序、数据和操作说明等。  
进程：进程是计算机为了完成任务实体而将其划分成的执行实体。即对于一个任务，计算机会将其划分成具体的、基本的执行单位，系统根据这些执行单位来进行调度和资源分配。  
线程：线程是进程进一步细分而成的独立可调度的执行单位。线程是程序执行流的最小单元，是系统独立调度的基本单位。  

- 进程的提出：1、解决了用户在计算机执行程序的过程中无法与计算机互动的问题。最初程序员在计算时需要一次向计算机提供所有数据，并等待计算机运行直到全部任务完成。这之中用户无法进行任何操作，也不知道任务的具体进度或有无bug，因此十分不便；而当计算机将作业划分为进程时，就可以按照进程进行资源分配和任务分配；2、提高了CPU的效率；CPU可以通过在极短的时间里轮换进行进程，从而实现多个任务并行。  
```
补充：进程运行开销大，电脑运行多个进程比运行多个线程麻烦很多
```
线程的提出：将进程进一步细化成可执行的单元，由于计算机单次分配给单个任务的时间极短，线程能够进一步提高效率。由于线程是进程在调度上的子单元，不像进程一样占有资源，故对它的调度所付出的开销就会小得多，因此线程能更高效的提高系统内多个程序间并发执行的程度，从而显著提高系统资源的利用率和吞吐量。  
  
  
### Q2：调研虚拟存储器的概念，描述其工作原理和作用
- 工作原理：虚拟存储器是计算机内存管理的技术，用以拓展存储空间。它将程序的内存分为多个不连续的部分，一部分存储在内存中，一部分存储在硬盘中，并通过算法调用这些存储，使得它们表观上是连续的。  
  简单来说，虚拟存储器的调度包括四个步骤：  
  1、CPU检查所需要的信息是否在主存储器内。  
  2、如该组号已在主存内，则执行4；如该组号不在主存内，则检查主存中是否有空闲区，如果没有，便将某个暂时不用的组调出送往辅存，以便将这组信息调入主存。  
  3、从辅存读出所要的组，并送到主存空闲区。  
  4、通过算法，从对应地址读取出所需信息。  
  
- 作用：1、由于有些时候运行的程序所需的存储空间比内存大，仅靠内存无法运行程序，虚拟内存可以使内存空间得到极大扩展，很大程度上避免了计算机可能面临的内存不足的问题。  
2、解决了仅有主存储器时不同进程调用同一内存的内存调度问题。
