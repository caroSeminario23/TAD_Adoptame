package com.adoptame.albergue2.repository;

import com.adoptame.albergue2.model.Mascota;
import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

@Repository
public interface MascotaRepository extends JpaRepository<Mascota, Integer> {
    
}
