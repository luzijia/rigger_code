<?php
class {{tablename}} extends Table
{
    public function __construct()
    {
        parent::__construct("{{tablename}}", "{{ pk }}");
    }

    public function add($info)
    {
        $this->addRecord($info);
    }

    public function get{{tablename}}Info(${{ pk }})
    {
        return $this->getRecord(${{pk}});
    }

    public function del{{tablename}}(${{pk}})
    {
        $sql = "delete from {$this->getTableName()} where {{ pk }}=?";
        return $this->Execute($sql, array(${{ pk }}));
    }

    public function update(${{ pk }},{{ fields_cond }})
    {
        $sql = "update {$this->getTableName()} set {{ fields_bind }}  where {{pk}}=?";
        $sql = "update {$this->getTableName()} set {{ fields_cond_val }}  where {{pk}}=?";
        return $this->Execute($sql, array({{ fields_cond }} ,${{pk}}));
    }
}
