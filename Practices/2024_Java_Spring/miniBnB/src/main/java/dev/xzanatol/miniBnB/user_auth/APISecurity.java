// Just testing the package
// package dev.xzanatol.miniBnB.Security;

// import org.springframework.context.annotation.Bean;
// import org.springframework.context.annotation.Configuration;
// import org.springframework.security.provisioning.JdbcUserDetailsManager;
// import org.springframework.security.provisioning.UserDetailsManager;
// import org.springframework.http.HttpMethod;
// import org.springframework.security.config.Customizer;
// import org.springframework.security.config.annotation.web.builders.HttpSecurity;
// import org.springframework.security.web.SecurityFilterChain;

// import javax.sql.DataSource;

// @Configuration
// public class APISecurity {

//     @Bean
//     public UserDetailsManager userDetailsManager(DataSource dataSource) {
//         JdbcUserDetailsManager jUserDetailsManager = new JdbcUserDetailsManager(dataSource);

//         jUserDetailsManager.setUsersByUsernameQuery("SELECT username, password, is_active FROM user WHERE username = ?;");

//         jUserDetailsManager.setAuthoritiesByUsernameQuery("SELECT username_id, role FROM roles WHERE username_id = ?;");

//         return jUserDetailsManager;
//     }

//     @Bean
//     public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
//         http.authorizeHttpRequests(
//           configurer -> configurer.requestMatchers(HttpMethod.GET,
//           "/properties")
//           .hasRole("USER"));

//         http.httpBasic(Customizer.withDefaults());

//         return http.build();
//     }
// }