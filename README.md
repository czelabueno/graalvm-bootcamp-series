# GraalVM Bootcamp Series

Welcome to the GraalVM Bootcamp! 🚀

![GraalVM Logo](images/img.png)

## About the Bootcamp

Are you ready to unlock the full potential of GraalVM? This is an immersive bootcamp experience where we dive deep into the world of GraalVM and explore its capabilities. This bootcamp consists of a serie of 3 talks that will equip you with the knowledge and skills to harness the power of GraalVM in your projects.

## Pre-requisites & Specs
This bootcamp used Oracle GraalVM for JDK 17 from SDKMAN! 
```
sdk install java 17.0.8-graal
sdk use java 17.0.8-graal
```
OR  you can download and install directly. Use this [link](https://download.oracle.com/graalvm/17/latest/graalvm-jdk-17_linux-x64_bin.tar.gz) for Linux x64.

## Talks

### 1. Starting with GraalVM
- 📽️ [Watch the Video](https://www.youtube.com/live/63tdF5XBpag)

In this session, we'll provide an overview, ecosystem and architecture of GraalVM and its significance in the world of programming. You'll learn about the various languages and runtimes supported by GraalVM, along with its unique features like high-performance JIT and AOT compilation for native image generation. During the talk, we also demonstrated live examples to showcase the concepts in action of:

- Just-In-Time (JIT) -  `graal` compiler in HotSpot JVM
    - Optimized machine code.
  - Ahead-Of-Time (AOT) - Native Image generation from:
    - `native-image Hello` (.class)
    - `native-image --module-path Hello.jar --module HelloModule` (java module)
    - `native-image -jar Hello.jar` (.jar)
  - Build tool: Maven and Gradle
    - Use of maven profiles `mvn clean package -Pnative`
    - Use of Tracing Agent to generate config json files.
    - Use of `reflections` and `resources` as dynamic features of Java.
  - Generation of polyglot native image using `python`, `javascript` and `java` languages in the same executable. 

### 2. Developing cloud native java applications 
- 📽️ [Watch the Video](https://www.youtube.com/live/s7iZX_7WQr4)

Building on the previous talks, this session will deep dive into the process of creating native images in AOT mode using most popular java frameworks. Learn how to transform your Java applications into standalone, lightweight executables that start up in milliseconds and consume minimal resources. During the talk, we walked through step-by-step live demos of development, testing, debugging & diagnostic and deploy into `AWS` and `Azure` serverless services.

- Native integration with most java frameworks:
  - `Springboot` (demo), `Micronaut` (demo), Quarkus, Helidon
    - Dynamic features: resource, reflection (with -agentlib)
    - Rest API Unit testing - Spring AOT & `JUnit 5`
    - Debugging GDB (Linux OS only), Diagnostic (Heap Dump, JFR snapshot with JVisualVM, use of `native-image-inspect` and Software Bill of Material).
- Container options for each native image executables type.
  - Dynamic libs executable - `docker` from linux `slim`
  - Mostly static executable - `docker` from `distroless`
  - Full static musl - `docker` from `scratch` or `alpine`
- CI/CD pipeline with `Github Actions`
- Deploy on cloud platform:
  - [x] Azure
  - [x] AWS
  - [ ] Oracle Cloud

### 3. Performance optimization of native image executable for high-scale environment
- 📽️ [Watch the Video](link_to_video_2)

Discover how to supercharge your applications with GraalVM's optimization techniques. We'll cover topics such as AOT compilation, Multi-thread Garbage Collector, Extreme compression with UPX, and how GraalVM can help improve the compute footprint of your applications. Throughout the session, we provided live demos to illustrate the optimization process for high-scale environments like `cloud` and `kubernetes`.

## Who Should Attend

Whether you're a seasoned developer or just starting your journey in programming, this bootcamp is designed for anyone interested in enhancing their understanding of GraalVM. If you're curious about boosting your application's performance, reducing resource usage, and exploring innovative programming languages, this bootcamp is for you.


---

## Share the GraalVM Bootcamp Experience!

Help us spread the word about the GraalVM Bootcamp and empower fellow developers to unlock the true potential of GraalVM. 🌟

By sharing this GitHub repository, you're not only contributing to the developer community but also giving others the chance to:

🚀 **Boost Application Performance:** Learn how GraalVM's optimization techniques can enhance the speed and efficiency of applications.

🔍 **Explore Innovative Programming Languages:** Discover the support for various languages and runtimes within GraalVM.

🎥 **Experience Live Demos:** Witness the power of GraalVM in action through live demonstrations during each talk.

💡 **Create Native Images:** Dive into the process of generating lightweight, fast-starting native executables.

✨ **Connect with Developers:** Engage with like-minded individuals who are excited about shaping the future of programming.

Sharing is caring! Let's build a stronger, more efficient developer community together. Click that **Share** button and let your peers know about this valuable learning opportunity. Together, we can revolutionize the way we develop and optimize applications.

[Link to GitHub Repo](https://github.com/czelabueno/graalvm-bootcamp-series)

Thank you for being a part of the GraalVM Bootcamp journey! 🙌🚀
