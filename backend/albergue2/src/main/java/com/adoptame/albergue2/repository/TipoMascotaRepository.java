package com.adoptame.albergue2.repository;

import com.adoptame.albergue2.model.TipoMascota;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TipoMascotaRepository extends JpaRepository<TipoMascota, Integer> {
    
}
