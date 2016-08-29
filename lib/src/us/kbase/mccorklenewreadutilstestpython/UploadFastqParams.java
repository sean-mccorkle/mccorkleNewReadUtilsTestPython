
package us.kbase.mccorklenewreadutilstestpython;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: UploadFastqParams</p>
 * <pre>
 * testing invocation of ReadsUtils
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "fwd_id",
    "wsid",
    "wsname",
    "objid",
    "name",
    "rev_id",
    "sequencing_tech"
})
public class UploadFastqParams {

    @JsonProperty("fwd_id")
    private String fwdId;
    @JsonProperty("wsid")
    private Long wsid;
    @JsonProperty("wsname")
    private String wsname;
    @JsonProperty("objid")
    private Long objid;
    @JsonProperty("name")
    private String name;
    @JsonProperty("rev_id")
    private String revId;
    @JsonProperty("sequencing_tech")
    private String sequencingTech;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("fwd_id")
    public String getFwdId() {
        return fwdId;
    }

    @JsonProperty("fwd_id")
    public void setFwdId(String fwdId) {
        this.fwdId = fwdId;
    }

    public UploadFastqParams withFwdId(String fwdId) {
        this.fwdId = fwdId;
        return this;
    }

    @JsonProperty("wsid")
    public Long getWsid() {
        return wsid;
    }

    @JsonProperty("wsid")
    public void setWsid(Long wsid) {
        this.wsid = wsid;
    }

    public UploadFastqParams withWsid(Long wsid) {
        this.wsid = wsid;
        return this;
    }

    @JsonProperty("wsname")
    public String getWsname() {
        return wsname;
    }

    @JsonProperty("wsname")
    public void setWsname(String wsname) {
        this.wsname = wsname;
    }

    public UploadFastqParams withWsname(String wsname) {
        this.wsname = wsname;
        return this;
    }

    @JsonProperty("objid")
    public Long getObjid() {
        return objid;
    }

    @JsonProperty("objid")
    public void setObjid(Long objid) {
        this.objid = objid;
    }

    public UploadFastqParams withObjid(Long objid) {
        this.objid = objid;
        return this;
    }

    @JsonProperty("name")
    public String getName() {
        return name;
    }

    @JsonProperty("name")
    public void setName(String name) {
        this.name = name;
    }

    public UploadFastqParams withName(String name) {
        this.name = name;
        return this;
    }

    @JsonProperty("rev_id")
    public String getRevId() {
        return revId;
    }

    @JsonProperty("rev_id")
    public void setRevId(String revId) {
        this.revId = revId;
    }

    public UploadFastqParams withRevId(String revId) {
        this.revId = revId;
        return this;
    }

    @JsonProperty("sequencing_tech")
    public String getSequencingTech() {
        return sequencingTech;
    }

    @JsonProperty("sequencing_tech")
    public void setSequencingTech(String sequencingTech) {
        this.sequencingTech = sequencingTech;
    }

    public UploadFastqParams withSequencingTech(String sequencingTech) {
        this.sequencingTech = sequencingTech;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((((((("UploadFastqParams"+" [fwdId=")+ fwdId)+", wsid=")+ wsid)+", wsname=")+ wsname)+", objid=")+ objid)+", name=")+ name)+", revId=")+ revId)+", sequencingTech=")+ sequencingTech)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
