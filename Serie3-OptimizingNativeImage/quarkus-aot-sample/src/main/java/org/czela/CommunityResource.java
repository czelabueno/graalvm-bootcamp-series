package org.czela;

import java.util.List;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

@Path("/community")
public class CommunityResource {

    private Community community;

    CommunityResource(){
        community = new Community("PeruJUG",List.of("Carlos Zela","Jose Diaz","Pepito"));
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Community community(){
        return this.community;
    }
    
}

record Community (String name, List<String> members){}
