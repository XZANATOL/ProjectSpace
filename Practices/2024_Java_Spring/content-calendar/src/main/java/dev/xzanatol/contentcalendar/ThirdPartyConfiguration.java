package dev.xzanatol.contentcalendar;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ThirdPartyConfiguration {

    @Bean
    public ThirdParty thirdPartyService() {
        return new ThirdParty();
    }

}