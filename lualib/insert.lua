local data = {}

local mysql = require "resty.mysql"

function data.connect()
    local db, err = mysql:new()
    if not db then
        ngx.log(ngx.ERR, "failed to instantiate mysql: ", err)
        return 
    end

    local ok, err, errcode, sqlstate = db:connect{
        -- host = "localhost",
        host = "mysql",
        -- port = 3306,
        database = "logs",
        user = "root",
        password = "!pyree2023",
        charset = "utf8",
        max_packet_size = 1024 * 1024,
    }

    if not ok then
        ngx.log(ngx.ERR, "failed to connect: ", err, ": ", errcode, " ", sqlstate)
        return
    end

    ngx.log(ngx.NOTICE, "connected to mysql.")

    return db
end

function data.insert(db, remote_addr, time_local, request_method, server_protocol, http_referer, request_uri, http_user_agent, body, http_cookie, sent_http_set_cookie, ml_prediction)
    local sql = string.format("INSERT INTO security_logs (remote_addr, time_local, request_method, server_protocol, http_referer, request_uri, http_user_agent, body, http_cookie, sent_http_set_cookie, ml_prediction) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        ngx.quote_sql_str(remote_addr),
        ngx.quote_sql_str(time_local),
        ngx.quote_sql_str(request_method),
        ngx.quote_sql_str(server_protocol),
        ngx.quote_sql_str(http_referer),
        ngx.quote_sql_str(request_uri),
        ngx.quote_sql_str(http_user_agent),
        ngx.quote_sql_str(body),
        ngx.quote_sql_str(http_cookie),
        ngx.quote_sql_str(sent_http_set_cookie),
        ngx.quote_sql_str(ml_prediction)
    )

    local res, err, errno, sqlstate = db:query(sql)

    if not res then
        ngx.log(ngx.ERR, "bad result: ", err, ": ", errno, ": ", sqlstate, ".")
        return 
    end

    return true
end

return data
