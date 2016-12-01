<?php
class ##tablename extends Table
{
    public function __construct()
    {
        parent::__construct("##tablename", "##pk");
    }

    public function add($info)
    {
        $this->addRecord($info);
    }

    public function get##tablenameInfo($##pk)
    {
        return $this->getRecord($##pk);
    }

    public function del##tablename($##pk)
    {
        $sql = "delete from {$this->getTableName()} where ##pk=?";
        return $this->Execute($sql, array($##pk));
    }

    public function update($##pk,##update_val_str)
    {
        $sql = "update {$this->getTableName()} set ##update_cond_str where ##pk=?";
        return $this->Execute($sql, array(##update_val_str,$##pk));
    }
}
