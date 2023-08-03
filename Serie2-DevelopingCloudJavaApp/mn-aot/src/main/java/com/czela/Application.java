package com.czela;

import io.micronaut.context.ApplicationContext;
import io.micronaut.context.annotation.Requires;
import io.micronaut.context.env.Environment;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.runtime.Micronaut;
import java.util.Arrays;
import java.util.List;
import java.util.Set;

public class Application {
    public static void main(String[] args) {
        Micronaut.run(Application.class, args);
    }
}

record Community (String name, List<String> members){}

@Controller
class CommunityHttpController {

    private Community community;

    CommunityHttpController(){
       List<String> members = Arrays.asList("Jose Diaz","Carlos Zela");
       community = new Community("PeruJUG",members);
    }

    @Get("/community")
    public Community getCommunity(){
        return this.community;
    }

    @Get("cloud-platform")
    @Requires (env = Environment.CLOUD)
    public Set<String> getHostCloud(){
        ApplicationContext ctx = ApplicationContext.builder().deduceCloudEnvironment(true).start();
        return ctx.getEnvironment().getActiveNames();
    }
}
