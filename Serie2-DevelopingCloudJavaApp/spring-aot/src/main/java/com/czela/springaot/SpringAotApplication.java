package com.czela.springaot;

import java.util.Arrays;
import java.util.List;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@SpringBootApplication
public class SpringAotApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringAotApplication.class, args);
	}

}

record Community (String name, List<String> members) {}

@Controller
@ResponseBody
class CommunityHttpController {

	private Community community;

	CommunityHttpController() {
		List<String> members = Arrays.asList("Jose Diaz","Carlos Zela","Ytalo Borja");
        community = new Community("PeruJUG", members);
    }

	@GetMapping("/community")
	Community community (){
		return  this.community;
	}

}

