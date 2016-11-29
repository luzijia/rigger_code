<?php
class ##tablename extends Table
{
    public function __construct()
    {
        parent::__construct("##tablename", "##pk");
    }

    public function add($info)
    {
        //默认表都有addtime和modtime字段
        $info['addtime'] =$info['modtime'] = date("Y-m-d H:i:s");
        $this->addRecord($info);
    }

    public function get##tablenameInfo($##pk)
    {
        return $this->getRecord($##pk);
    }

    public function get##tablenameList($condition = "", $params = array(), $start = 0, $num = 0, $order = "")
    {
        $sql = "select * from {$this->getTableName()}";
        $sql.= $condition != "" ? " where " . $condition : "";
        $sql.= " order by " . ($order != "" ? $order : $this->getPrimary() . " desc");
        $sql.= $num > 0 ? " limit $start, $num" : " limit 0,10 ";

        $lists = $this->getAll($sql, $params);
        $total = $this->getOne("select count(*) as total from ".$this->getTableName().($condition != "" ? "
        where " . $condition : ""),$params);

        return array($total, $lists);
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
