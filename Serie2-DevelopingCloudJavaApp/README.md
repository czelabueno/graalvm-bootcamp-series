# GraalVM Bootcamp Series

## Serie 2. Developing cloud native java applications
- 📽️ [Watch the Video](https://www.youtube.com/live/s7iZX_7WQr4)


Building on the previous talks, this session will deep dive into the process of creating native images in AOT mode using most popular java frameworks. Learn how to transform your Java applications into standalone, lightweight executables that start up in milliseconds and consume minimal resources. During the talk, we walked through step-by-step live demos of development, testing, debugging & diagnostic and deploy into `AWS` and `Azure` serverless services.

### Clone this repo
```
git clone https://github.com/czelabueno/graalvm-bootcamp-series.git
cd ./Serie2-DevelopingCloudJavaApp
```

### Springboot AOT - Development
- Dynamic features: resource, reflection (with -agentlib)

### Springboot AOT - Unit & Integration testing
- Rest API Unit testing - Spring AOT & `JUnit 5`

### Springboot AOT - Debugging
- Debugging GDB (Linux OS only), Diagnostic (Heap Dump, JFR snapshot with JVisualVM, use of `native-image-inspect` and Software Bill of Material).

### Container options for each native image executables type - Packaging
- Dynamic libs executable - `docker` from linux `slim`
- Mostly static executable - `docker` from `distroless`
- Full static musl - `docker` from `scratch` or `alpine`

### Cloud platform serverless - Deploying
- CI/CD pipeline with `Github Actions`
- Deploy on cloud platform:
    - [x] Azure
    - [x] AWS
    - [ ] Oracle Cloud