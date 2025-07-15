package com.adoptame.albergue2.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.*;

@Configuration
public class CorsConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
            .allowedOrigins("*") // Especificar el frontend
            .allowedMethods("GET", "POST")
            .allowedHeaders("*");
    }
}
