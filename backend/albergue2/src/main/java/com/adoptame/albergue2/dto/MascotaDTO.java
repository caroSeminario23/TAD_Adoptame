package com.adoptame.albergue2.dto;

import java.math.BigDecimal;
import java.time.OffsetDateTime;

//import com.adoptame.albergue2.model.Raza;
//import com.adoptame.albergue2.model.TipoMascota;

public class MascotaDTO {
    private Integer idMascota;
    private String nombre;
    private String foto;
    private java.sql.Date fecNacimiento;
    private String sexo;
    private BigDecimal estatura;
    private BigDecimal peso;
    private Integer idTipoMascota;
    private Integer idRaza;
    private OffsetDateTime fecIngreso;
    private Boolean adoptado;
    private Boolean discapacidad;

    public MascotaDTO() {}

    public MascotaDTO(Integer idMascota, 
                    String nombre, 
                    String foto, 
                    java.sql.Date fecNacimiento, 
                    String sexo,
                    BigDecimal estatura, 
                    BigDecimal peso, 
                    Integer idTipoMascota, 
                    Integer idRaza,
                    OffsetDateTime fecIngreso, 
                    Boolean adoptado, 
                    Boolean discapacidad) {
        this.idMascota = idMascota;
        this.nombre = nombre;
        this.foto = foto;
        this.fecNacimiento = fecNacimiento;
        this.sexo = sexo;
        this.estatura = estatura;
        this.peso = peso;
        this.idTipoMascota = idTipoMascota;
        this.idRaza = idRaza;
        this.fecIngreso = fecIngreso;
        this.adoptado = adoptado;
        this.discapacidad = discapacidad;
    }

    // Getters y setters
    public Integer getIdMascota() { 
        return idMascota; 
    }
    public void setIdMascota(Integer idMascota) { 
        this.idMascota = idMascota; 
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getFoto() {
        return foto;
    }
    public void setFoto(String foto) {
        this.foto = foto;
    }
    public java.sql.Date getFecNacimiento() {
        return fecNacimiento;
    }
    public void setFecNacimiento(java.sql.Date fecNacimiento) {
        this.fecNacimiento = fecNacimiento;
    }
    public String getSexo() {
        return sexo;
    }
    public void setSexo(String sexo) {
        this.sexo = sexo;
    }
    public BigDecimal getEstatura() {
        return estatura;
    }
    public void setEstatura(BigDecimal estatura) {
        this.estatura = estatura;
    }
    public BigDecimal getPeso() {
        return peso;
    }
    public void setPeso(BigDecimal peso) {
        this.peso = peso;
    }
    public Integer getIdTipoMascota() {
        return idTipoMascota;
    }
    public void setTipoMascota(Integer idTipoMascota) {
        this.idTipoMascota = idTipoMascota;
    }
    public Integer getIdRaza() {
        return idRaza;
    }
    public void setRaza(Integer idRaza) {
        this.idRaza = idRaza;
    }
    public OffsetDateTime getFecIngreso() {
        return fecIngreso;
    }
    public void setFecIngreso(OffsetDateTime fecIngreso) {
        this.fecIngreso = fecIngreso;
    }
    public Boolean getAdoptado() {
        return adoptado;
    }
    public void setAdoptado(Boolean adoptado) {
        this.adoptado = adoptado;
    }
    public Boolean getDiscapacidad() {
        return discapacidad;
    }
    public void setDiscapacidad(Boolean discapacidad) {
        this.discapacidad = discapacidad;
    }
}
