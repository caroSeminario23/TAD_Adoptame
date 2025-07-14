package com.adoptame.albergue2.repository;

import com.adoptame.albergue2.model.Raza;
import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

@Repository
public interface RazaRepository extends JpaRepository<Raza, Integer> {
    
}
